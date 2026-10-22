# Vulkan Backends: From First Principles to End-to-End Engineering

**Research date:** 17 October 2026  
**Audience:** A developer starting with GPU software terminology and progressing toward principal-engineer-level architectural reasoning.  
**Focus:** Vulkan, Mesa, NVIDIA, AMD, Qualcomm, graphics, compute, and the contracts between software layers.

This guide builds a complete architectural mental model. It is not a reproduction of the Vulkan specification or an exhaustive list of extensions. Hardware support and implementation details must be checked against a particular release. Examples are explanatory; no GPU application or benchmark was executed for this guide.

**Reading order**

- **Foundations:** sections 1-5.
- **Execution and correctness:** sections 6-14.
- **Architecture, diagnosis, and performance:** sections 15-21.
- **Practical learning sequence and reference:** sections 22-24.

The central principle is:

> Identify the layer, identify the owner, identify the contract, and identify the evidence that the contract is being satisfied.

## 1. The one-page mental model

A CPU runs your application. The application arranges work for a GPU. Software prepares commands, resources, and executable GPU programs. The operating-system driver and GPU hardware then execute that work asynchronously.

Do not think of a single opaque "GPU call." There are three related flows:

```text
CONTROL / COMMAND FLOW
Application
  -> application renderer or compute backend
  -> Vulkan API calls
  -> loader dispatch and optional layers
  -> selected Vulkan user-space driver
  -> OS kernel driver interfaces
  -> GPU command processor / scheduling machinery
  -> GPU execution

SHADER / PROGRAM FLOW
GLSL, HLSL, or another supported shader language
  -> a compiler that emits Vulkan-compatible SPIR-V
  -> the Vulkan driver's shader compiler
  -> GPU-specific machine instructions

RESOURCE / DATA FLOW
Host data, images, model weights, or previously computed GPU data
  -> allocated and bound buffer/image memory
  -> upload or direct host-visible access where appropriate
  -> GPU reads and writes
  -> another GPU pass, display presentation, or CPU readback
```

These flows meet at execution. A shader needs data; a command dispatches that shader; synchronization establishes when its inputs are valid and when its results may be consumed.

**CPU-side API completion is not GPU completion.** Recording a dispatch does not run it. Submitting a command buffer does not usually wait for it to finish. Presenting an image does not mean the image is already on the screen. [S01] [S03] [S06]

## 2. The names belong to different categories

| Term | Category | Meaning |
|---|---|---|
| Vulkan | API specification | Defines graphics and compute functionality, objects, commands, and correctness rules |
| OpenGL | Graphics API | A different API with a more driver-managed, stateful programming model; modern versions also support compute |
| OpenGL ES | Graphics API family | Graphics interfaces designed for embedded/mobile systems |
| OpenCL | Compute API | Parallel computation on devices for which a suitable implementation exists |
| GLSL / HLSL | Shader languages | Languages used to write programs that will execute on graphics/compute hardware |
| SPIR-V | Intermediate representation | A binary program representation consumed by Vulkan shader implementations |
| Mesa | Software project | Open-source API implementations, drivers, compilers, and shared infrastructure |
| RADV / Turnip / NVK | Vulkan implementations | Mesa Vulkan drivers for AMD, Qualcomm Adreno, and NVIDIA hardware respectively |
| ACO / ir3 / NAK | Compiler components | Hardware-targeted compiler infrastructure, not alternative graphics APIs |
| amdgpu / nouveau / msm | Linux kernel drivers | OS-level hardware interfaces; not Vulkan API implementations |
| CUDA | NVIDIA compute platform/API family | General-purpose GPU programming and accelerated libraries |
| ROCm / HIP | AMD compute stack / programming layer | A separate GPU-compute ecosystem; not required just to use Radeon Vulkan |
| QNN | Qualcomm graph/backend interface | An AI execution path that can target supported Qualcomm accelerators |
| Backend | Relative architectural term | The implementation selected by a particular software layer |

Vulkan is not inherently a GPU brand. A Vulkan implementation can target hardware, translate to another API, or execute in software on a CPU.

OpenGL, Vulkan, and OpenCL are not consecutive stages. Their programming models differ, although a translation layer can intentionally implement one API using another. [S02] [S03] [S14] [S19] [S20] [S21] [S23]

## 3. The six meanings of "Vulkan backend"

The word "backend" is meaningless without identifying its frontend.

| Context | Frontend receives | Backend does | Example |
|---|---|---|---|
| Application renderer | Engine rendering operations | Emits Vulkan calls instead of another graphics API | An engine's Vulkan versus Direct3D renderer |
| Compute/inference library | Tensor or numerical operations | Selects shaders, resources, and Vulkan dispatches | A Vulkan compute backend in an inference library |
| API translation layer | Calls from another API | Implements those calls using Vulkan | Zink, ANGLE's Vulkan renderer, DXVK |
| Vulkan driver | Vulkan API calls and SPIR-V | Implements Vulkan on a target device | RADV, Turnip, NVK, vendor drivers |
| Shader compiler | Intermediate representation | Generates target machine instructions | RADV's ACO compiler backend |
| Window-system integration | Surface/presentation requests | Integrates with the platform window/display system | Wayland, X11, Win32, Android surface integration |

For example:

```text
Game engine's Vulkan backend
  -> Vulkan loader
  -> Mesa RADV driver
  -> ACO compiler backend for shaders
  -> amdgpu kernel driver
  -> AMD GPU
```

This sentence contains two different kinds of backend. Neither is the same as "Mesa."

An engineer should resolve a statement such as "the Vulkan backend is broken" into something testable: device discovery failed, the engine emitted invalid commands, a shader was miscompiled, a resource dependency was missing, or presentation failed. [S03] [S19] [S23] [S25] [S27] [S36]

## 4. The complete application-to-hardware stack

```text
USER SPACE: CPU process
------------------------------------------------------------
Application / engine / inference library
    |
    | Optional engine abstraction:
    | render hardware interface or tensor-operation interface
    v
Application Vulkan backend
    |
    | Vulkan calls, object handles, descriptors, SPIR-V
    v
Vulkan loader + dispatch chains
    |
    | Optional validation, capture, tracing, or overlay layers
    v
Vulkan user-mode driver / ICD
    |  shader compilation
    |  resource implementation
    |  command-stream generation
    |  OS submission
------------------------------------------------------------
KERNEL SPACE: operating system
GPU memory management, scheduling, isolation, driver interfaces
------------------------------------------------------------
DEVICE
Firmware and command processors, as applicable
    |
GPU shader cores + caches + graphics/transfer/other engines
    |
Memory results
    +--> another GPU operation
    +--> display/presentation path
    +--> CPU-visible readback
```

**User space** is where ordinary application code runs. **Kernel space** is the privileged operating-system environment controlling device access and system resources.

The boundary matters:

- A Vulkan driver normally compiles shaders in user space, not by handing GLSL to the kernel.
- A recorded Vulkan command does not necessarily cause a system call immediately.
- A single Vulkan call can expand into many hardware commands.
- The kernel is not a Vulkan validator and does not understand all application resource dependencies.
- The operating system and firmware still participate in execution; Vulkan does not bypass them.

The loader is chiefly discovery and dispatch infrastructure, not a shader optimizer. Layers can intercept calls, but they are optional and are not the selected GPU driver. The drawing is a conceptual call chain; actual loader trampolines and dispatch tables avoid unnecessary work on many device calls. [S03] [S19] [S30]

## 5. NVIDIA, AMD, Qualcomm, and translation routes

### Native-driver examples

| Target | Vulkan implementation | Typical lower-level route | Important boundary |
|---|---|---|---|
| AMD on Linux | Mesa RADV | amdgpu kernel driver | RADV is user space; amdgpu is kernel space |
| AMD on Windows | AMD vendor Vulkan implementation | Windows graphics driver stack / WDDM | Do not describe this as Linux RADV |
| NVIDIA vendor stack | NVIDIA Vulkan implementation | NVIDIA's platform driver stack | Vulkan does not require calling CUDA |
| NVIDIA Mesa stack | NVK | Nouveau-related Linux kernel interfaces | NVK/Nouveau is distinct from NVIDIA's vendor Vulkan stack |
| Qualcomm supported Mesa stack | Turnip | Supported Adreno platform/kernel integration, such as DRM/msm on Linux | Turnip is a GPU driver, not the Hexagon NPU runtime |
| Qualcomm vendor stack | Qualcomm/OEM Vulkan implementation | Product-specific Android or Windows driver stack | Do not assume its internals are Mesa/ir3 |
| Software Vulkan | Lavapipe or SwiftShader | CPU execution | Vulkan device discovery alone does not prove hardware GPU acceleration |

Exact GPU generations, kernels, APIs, and features are release-dependent. Do not apply a desktop installation recipe to an Android OEM image.

NVIDIA's open Linux kernel modules and Nouveau are not interchangeable names. Likewise, AMD's GPU kernel driver does not mean the Ryzen AI NPU uses the same execution path. [S03] [S19] [S20] [S21] [S30] [S35] [S38]

### Translation examples

```text
OpenGL application
  -> Mesa OpenGL frontend + Zink
  -> Vulkan implementation
  -> target hardware

OpenGL ES / WebGL integration
  -> ANGLE with its Vulkan renderer selected
  -> Vulkan implementation
  -> target hardware

Direct3D 9/10/11 application
  -> DXVK
  -> Vulkan implementation
  -> target hardware

Direct3D 12 application
  -> vkd3d-proton
  -> Vulkan implementation
  -> target hardware

Vulkan application using a Vulkan-over-Metal implementation
  -> translation driver
  -> Metal and its platform driver
  -> Apple hardware
```

These are architectural examples, not universal compatibility guarantees. Translation support depends on both the translator and its underlying implementation.

Mesa's Lavapipe and LLVMpipe are easy to confuse: Lavapipe exposes Vulkan in software; LLVMpipe is associated with Mesa's Gallium software-rasterization path used for OpenGL. A name containing "Vulkan" is not proof that a physical GPU is doing the work.

MoltenVK is a Vulkan-over-Metal example, but its current upstream README contains deprecation and platform-specific guidance, including a recommendation for KosmicKrisp on Apple Silicon. It should not be presented as a timeless deployment recommendation. [S03] [S23] [S24] [S25] [S26] [S27] [S28]

## 6. What happens when an application starts

### 6.1 Discovery

1. The process loads a Vulkan loader, commonly `vulkan-1.dll` on Windows or `libvulkan.so.1` on Linux.
2. The loader discovers available driver implementations using platform-specific mechanisms.
3. On desktop systems, driver manifests help identify implementation libraries. Android has its own loader/driver integration; do not assume the same desktop manifest procedure.
4. Requested and implicit layers are considered.
5. The application creates a Vulkan instance and enumerates physical devices exposed through available implementations.

An ICD means **Installable Client Driver**. Multiple ICDs can coexist. A driver can expose multiple devices; alternative drivers can sometimes expose the same underlying hardware through different implementations.

### 6.2 Selection

The application, not a magical "fastest GPU" rule in Vulkan, selects its device.

A robust selection policy checks:

- Device identity and type.
- Driver identity and version.
- Required core API version.
- Queue-family capabilities.
- Required extensions and enabled features.
- Memory heaps/types and resource limits.
- Presentation support for the actual surface, if graphics presentation is required.
- Application-specific format, shader, numerical, and interoperability requirements.

A compute queue need not support presentation. A graphics-capable device is not automatically suitable for every window-system surface.

### 6.3 Supported is not enabled

Headers containing an enum or function do not prove runtime support. These are different:

```text
SDK/header version
Loader-supported instance version
Physical-device API version
Supported extensions and feature bits
Features/extensions actually enabled for this instance/device
```

Query first, enable the required contract, then use it. Feature structures commonly travel through `pNext` chains. Some functionality becomes core in a newer Vulkan version; select a valid core or extension path rather than enabling names blindly.

Do not decode every vendor's `driverVersion` using one assumed version-number format. Prefer supported driver property fields and vendor documentation.

### 6.4 Driver overrides are diagnostic tools

The Khronos desktop loader supports `VK_DRIVER_FILES`. The older `VK_ICD_FILENAMES` is deprecated. Driver-select and driver-disable filters operate on discovered manifests and depend on loader support.

These controls do not add hardware support or turn a vendor driver into another vendor's driver. They can also make all devices disappear when configured incorrectly. Elevated processes have additional restrictions on environment-based driver loading.

Prefer application device selection for normal operation. Use process-local overrides only for a deliberate diagnostic comparison, and record them in the reproduction environment. [S03] [S04] [S05] [S06]

## 7. The Vulkan object model

| Object | What it represents | Common mistake |
|---|---|---|
| `VkInstance` | Application's connection to instance-level Vulkan functionality | Treating it as an already-selected GPU |
| `VkPhysicalDevice` | An enumerated physical-device implementation | Assuming enumeration order means performance order |
| `VkDevice` | Logical interface created for selected device capabilities | Assuming unsupported features become available after creation |
| `VkQueue` | Submission interface for a queue family | Assuming each queue is a dedicated hardware engine |
| `VkCommandPool` | Allocator/owner for command buffers of a queue family | Concurrently using it without required host synchronization |
| `VkCommandBuffer` | Recorded commands | Assuming recording is execution |
| `VkBuffer` | A buffer resource with declared usage | Assuming creation alone provides backing storage |
| `VkImage` | A structured image resource | Confusing format, tiling, layout, and allocation |
| `VkDeviceMemory` | A memory allocation used to back resources | Assuming every allocation is separate physical VRAM |
| Image/buffer view | A particular interpretation/range of a resource | Reusing an incompatible format/range |
| Descriptor set/layout | Resource binding information and its interface | Treating a descriptor update as a data upload |
| `VkPipelineLayout` | Descriptor and push-constant interface | Ignoring compatibility with the shader/pipeline |
| `VkPipeline` | Executable pipeline configuration | Assuming a shader module alone is sufficient to dispatch |
| `VkFence` | Host-observable completion primitive | Reusing it without managing its signaled state |
| `VkSemaphore` | Dependency primitive between operations | Assuming a frame fence covers presentation waits |
| `VkSurfaceKHR` | Platform presentation surface | Assuming an offscreen compute job requires a surface |
| `VkSwapchainKHR` | Presentation image-management interface | Assuming its image count equals frames in flight |

A `VkDevice` normally targets a selected physical device; explicitly supported device-group functionality is a separate advanced topic.

Ownership and lifetime are fundamental: if pending GPU work references a resource, destroying or recycling that resource prematurely is invalid even if the CPU has finished recording commands. [S01] [S03] [S06] [S11] [S32]

## 8. Shader compilation and hardware command generation

### 8.1 Two programs are involved

The host program runs on the CPU. Shaders run on the GPU.

```text
C/C++ application -> CPU compiler -> host executable

GLSL/HLSL/Slang shader
  -> appropriate shader frontend
  -> Vulkan-compatible SPIR-V
  -> driver-specific compilation/lowering
  -> target GPU ISA
```

SPIR-V is not the GPU's final machine code. It describes operations and capabilities for a target execution environment. Valid generic SPIR-V is not automatically valid for Vulkan or for every device's enabled capabilities.

Pipeline creation can trigger expensive compilation and optimization. The exact compilation schedule is implementation-dependent; some implementations use additional deferred or cached work. Do not assume shader-module creation is the only compilation point.

### 8.2 Mesa examples

| Driver | Simplified shader path |
|---|---|
| RADV | SPIR-V -> NIR transformations/lowering -> ACO -> AMD GPU ISA |
| NVK | Mesa shader IR/lowering -> NAK compiler backend -> NVIDIA GPU ISA |
| Turnip | Mesa shared Freedreno shader infrastructure, including ir3 -> Adreno instructions |

**NIR** is a Mesa intermediate representation. **Lowering** rewrites a high-level operation into operations the next layer or hardware can implement.

Compiler work can include constant folding, dead-code elimination, instruction selection, instruction scheduling, register allocation, and spill handling. More live values can consume more registers; that can reduce the number of simultaneously resident waves.

RADV's current documentation identifies ACO as the normal compiler backend. Its LLVM path is described as testing/hardware-bring-up infrastructure, not the recommended normal user path. Do not generalize that Mesa always compiles every shader through LLVM.

Proprietary vendor implementations may use different internal IRs and compilers. Do not infer their internals from the public Mesa equivalents. [S14] [S15] [S16] [S19] [S20] [S21] [S22]

### 8.3 A command buffer is not a shader

The shader is a program. A command buffer says which programs and resources to use, what to draw/dispatch/copy, and which dependencies apply.

In RADV, command recording produces hardware command streams. Graphics/compute queues use AMD packet formats such as PM4; other engines use other formats. Submitted command streams eventually instruct the GPU command processor to launch shader work and use fixed-function hardware.

There is no universal one-Vulkan-call-to-one-hardware-packet relationship. Setting up one operation can require multiple packets and state updates. [S19]

### 8.4 Caches are optimizations, not portable executables

Pipeline caches can reduce repeated compilation. Their data is implementation-specific. Check compatibility, including the relevant cache identity and application configuration, before reuse.

A robust cache policy distinguishes:

- Shader source/intermediate artifacts.
- Application pipeline configuration keys.
- Driver pipeline-cache data.
- Driver/device/version compatibility.

Corrupt or incompatible cache data should trigger a diagnosed rebuild, not an unexplained crash or a false claim that cached binaries are universally portable. [S16]

## 9. Memory: resources, allocation, placement, and visibility

### 9.1 Creation and backing storage are separate

A typical resource path is:

```text
Create buffer/image with the required usage
  -> query memory requirements
  -> select a compatible memory type
  -> allocate or suballocate memory
  -> bind that memory to the resource
  -> initialize data and establish dependencies
```

Memory requirements include size, alignment, and compatible memory-type bits. A heap describes a memory pool; a memory type combines placement with properties.

Large allocations with suballocation are often preferable to one allocation per small resource. Vulkan Memory Allocator is an established helper for this problem; using it does not remove synchronization or resource-lifetime obligations. [S07] [S32]

### 9.2 Important properties

| Property | Meaning | Does not mean |
|---|---|---|
| `DEVICE_LOCAL` | Memory preferred/local for device access | Always physically separate VRAM |
| `HOST_VISIBLE` | CPU mapping is supported | GPU work using it has finished |
| `HOST_COHERENT` | Specified host cache-management operations can be omitted | CPU/GPU execution is automatically synchronized |
| `HOST_CACHED` | Host caching properties suitable for some CPU access patterns | Always the best upload memory |

A discrete GPU commonly has dedicated memory and uses staging transfers. An integrated/UMA GPU can expose memory that is both device-local and host-visible. Some discrete systems also expose host-visible device-local memory. Query the actual properties rather than using a vendor-name heuristic.

### 9.3 Upload

Typical discrete-GPU upload:

```text
CPU writes mapped staging memory
  -> flush the relevant range if it is non-coherent
  -> submit a copy to device-local memory
  -> transfer-write to consumer-read dependency
  -> shader consumes the data
```

For ordinary host writes completed before submission, queue submission provides the relevant host-write ordering/domain operation described by the specification. A redundant pre-copy host pipeline barrier is not the missing ingredient. Correct host synchronization and non-coherent flushing still matter.

UMA can remove the need for this copy when a suitable allocation is directly accessible. It does not remove resource lifetimes, access dependencies, or cache-management rules. [S07] [S10] [S12]

### 9.4 Readback

For data written into a host-visible allocation:

```text
GPU shader writes
  -> shader-write to host-read memory dependency
  -> completion signal
  -> CPU waits for completion
  -> invalidate non-coherent mapped range if required
  -> CPU reads
```

For device-local output not directly readable by the CPU, copy to a readback buffer first, with the corresponding shader-to-transfer and transfer-to-host dependencies.

Mapping/unmapping is not synchronization. Unmapping does not implicitly flush non-coherent host writes. Mapping does not implicitly invalidate stale host cache contents.

Flush/invalidate ranges must respect allocation bounds and `nonCoherentAtomSize` rules. Atom-size interactions can create hazards between neighboring suballocations, so alignment is a correctness issue, not only a performance issue. [S10] [S12] [S13]

### 9.5 Four different meanings often confused as "layout"

1. **Data layout:** member offsets, array stride, matrix layout, and alignment shared between host code and shaders.
2. **Image format:** the interpretation of texels, such as channel organization and numeric type.
3. **Image tiling:** implementation-dependent storage organization, such as optimal versus linear tiling.
4. **Image layout:** Vulkan's logical usage/layout state, such as shader-read-only, transfer destination, color attachment, or present source.

`GENERAL` image layout is not "synchronization-free mode." A descriptor pointing to an image does not transition that image into the required layout.

Host structure packing must match shader expectations; a C++ structure that merely looks similar to a GLSL block can have different offsets or padding. [S08] [S10]

## 10. Descriptors and pipelines: connecting programs to resources

A shader needs a defined interface to its buffers, images, samplers, and small parameters.

- A **descriptor** describes a resource binding or resource view. It does not normally contain the entire texture or model tensor.
- A **descriptor-set layout** defines the binding types and structure.
- A **descriptor set** supplies concrete bindings under that layout.
- A **pipeline layout** defines the shader-visible descriptor-set interfaces and push-constant ranges.
- **Push constants** are a small, explicitly limited parameter mechanism; they are not a replacement for large buffers.
- A **pipeline** combines executable shader stages and the applicable pipeline state.

In a graphics pipeline, state includes relationships to vertex data, primitive processing, rasterization, depth/stencil, blending, and render targets, with some state made dynamic.

A compute pipeline uses a compute shader and its resource interface. It has no requirement to create a window or run vertex/fragment stages.

Descriptor indexing, descriptor buffers, and shader-object extensions can change implementation choices. They do not remove the need for capability checks, compatible interfaces, synchronization, or valid lifetimes.

Do not overwrite descriptor or parameter data while an in-flight operation may still read it unless the specific update rules and synchronization permit it. Use versioned/per-frame bindings or another explicitly safe design. [S01] [S05] [S08] [S17]

## 11. Queues, command buffers, and CPU threading

A queue family advertises a set of capabilities and available queues. Common capabilities include graphics, compute, and transfer.

Important distinctions:

- A **queue family** is a capability/compatibility grouping.
- A **queue** is a submission interface.
- A **hardware engine** is a physical execution resource.
- The mapping from Vulkan queues to hardware is implementation-defined.

Multiple queues do not guarantee independent engines or concurrent execution. A second queue can contend for the same shader cores, caches, bandwidth, or power budget.

Likewise, same-queue submission order is not a blanket memory dependency. Pipeline stages and operations can overlap. Resource hazards still require the applicable dependencies.

Command-buffer lifecycle is broadly:

```text
Allocate -> record -> executable -> submit/pending
         -> completion -> reset/re-record or free
```

Follow the exact usage flags and pool/reset rules; do not reset or destroy a pending command buffer.

### Multithreading

Vulkan enables parallel host-side work, but objects designated **externally synchronized** require application-side synchronization. Examples include particular queue, command-pool, and descriptor-pool accesses.

A common architecture gives each recording worker its own command pools, often separated further by in-flight frame/work batch. Submission to a shared queue is serialized according to Vulkan's host synchronization requirements.

More CPU recording threads do not automatically create more GPU parallelism. Host threading and device synchronization are separate problems. [S01] [S06]

## 12. Synchronization: the core correctness contract

Always separate four questions:

1. **Execution:** which operation must happen before another?
2. **Memory:** when are writes available and visible to the consumer?
3. **Image state:** which image layout is required?
4. **Ownership/lifetime:** which queue family or operation can access the resource, and when may it be reused?

### 12.1 Hazards

| Relationship | Example | Typical requirement |
|---|---|---|
| Read after write | Compute writes data later read by another shader | Execution and memory dependency |
| Write after read | A later operation overwrites data still being read | Execution ordering; additional rules can apply for layout or other accesses |
| Write after write | Two passes overwrite the same region | Appropriate execution and memory dependency |
| Read after read | Two shaders only read immutable data | Usually no dependency for the reads alone; layout/ownership requirements still apply |

### 12.2 Primitives

| Primitive | Role |
|---|---|
| Pipeline barrier | Establishes dependencies between specified stages/accesses; buffer/image barriers can carry resource-specific information |
| Binary semaphore | An operation signals, another waits; commonly used for queue and presentation dependencies |
| Timeline semaphore | Monotonically increasing values support GPU and host coordination when available/enabled |
| Fence | Lets the CPU observe completion of submitted work |
| Event | More advanced split dependency mechanism |

A useful starting point is synchronization2: the core Vulkan 1.3 interface or the appropriate enabled extension path. A dependency specifies producer stage/access and consumer stage/access, not simply "wait for the GPU."

For example:

```text
Producer: COMPUTE_SHADER, SHADER_WRITE
Consumer: COMPUTE_SHADER, SHADER_READ
```

If the consumer is a copy, an indirect dispatch, vertex fetching, or CPU readback, the consumer scope must describe that actual operation instead.

Do not solve every hazard with maximum-scope barriers or `vkDeviceWaitIdle`. Broad serialization can hide missing reasoning and destroy overlap.

### 12.3 Cross-queue work

Separate queues generally need semaphore dependencies. If an exclusively shared resource moves between different queue families, queue-family ownership transfers may also be required.

These are not the same operation:

- A semaphore establishes a dependency.
- An image barrier can transition layout.
- A queue-family transfer changes ownership where required.

Concurrent sharing can avoid specific ownership transfers but does not remove data-hazard synchronization.

### 12.4 Host coherence is not completion

`HOST_COHERENT` does not permit the CPU to overwrite a buffer while the GPU is reading it. A valid pattern is a ring buffer whose regions are reused only after associated completion values have retired.

### 12.5 Workgroup barriers are not whole-dispatch barriers

A shader workgroup barrier coordinates invocations within its workgroup. It does not synchronize arbitrary workgroups across a dispatch.

An algorithm needing a global phase boundary often uses multiple dispatches with an explicit dependency between them. Avoid ad hoc cross-workgroup spin barriers: scheduling and forward-progress assumptions can make them invalid or deadlock-prone. [S06] [S09] [S10] [S17] [S18]

## 13. End-to-end graphics: one frame

### 13.1 Initialization

```text
Create window and appropriate surface integration
  -> create instance and development diagnostics
  -> enumerate/select physical device
  -> verify graphics and surface presentation support
  -> create logical device and queues
  -> create swapchain and image views
  -> create required depth/other render resources
  -> create shaders, layouts, pipelines, resource bindings
  -> create per-frame command and synchronization resources
```

A **surface** connects to a window-system presentation target. A **swapchain** manages images exchanged with the presentation system.

Swapchain format, color space, extent, image usage, present mode, image count, and surface transform must come from supported configurations. On mobile systems, orientation and surface pre-rotation can materially affect efficiency.

Traditional render passes and dynamic rendering provide different ways of describing rendering operations. Dynamic rendering simplifies certain setup; it does not infer resource synchronization for you. [S05] [S29] [S37]

### 13.2 Frame execution

1. Wait for the selected frame slot's previously submitted GPU work before recycling that slot's resources.
2. Acquire a swapchain image.
3. Handle acquisition results correctly.
4. Prepare safe per-frame data and record commands.
5. Establish required image layouts and dependencies.
6. Bind pipeline, descriptors, vertex/index data, and dynamic state.
7. Record rendering and draw commands.
8. Transition the image to the required presentation layout.
9. Submit, waiting for image acquisition at the correct scope.
10. Signal render completion for presentation and completion for frame-resource reuse.
11. Queue presentation.
12. Handle resize, suboptimal, out-of-date, surface-loss, or device errors under explicit policies.

Once executed, a simplified rasterization flow is:

```text
Vertex input / generated vertices
  -> vertex processing
  -> primitive assembly and rasterization
  -> fragment shading
  -> depth/stencil/blending as applicable
  -> render-target image
  -> compositor or direct presentation path
  -> display scanout
```

Actual pipelines may add tessellation, geometry, mesh shading, ray tracing, or other operations. Early/late tests and tile-based execution mean this sketch is not a literal universal hardware schedule.

### 13.3 Frame slot is not image index

These are independent:

```text
frameSlot: chosen by the application's in-flight resource ring
imageIndex: returned by swapchain acquisition
```

The application may use two frames in flight with three swapchain images.

For the standard binary-semaphore WSI path, a straightforward safe pattern uses acquisition and frame-completion resources per frame slot, but presentation-wait semaphores per swapchain image.

**Waiting for a render submission's fence does not prove the presentation operation has finished consuming its wait semaphore.** Khronos documents safe reuse through image reacquisition and the required acquisition wait, or through suitable presentation extensions.

Explanatory pseudocode, assuming one compatible graphics/present queue:

```text
wait for frame[frameSlot].completionFence

result, imageIndex = acquire image using frame[frameSlot].imageAvailable
if result is OUT_OF_DATE:
    request safe swapchain recreation
    leave without resetting the completion fence
if result is neither SUCCESS nor SUBOPTIMAL:
    report and handle the failure

recycle and record this frame's command resources
record required barriers, draws, and transition to present layout

reset frame[frameSlot].completionFence immediately before submission
submit:
    wait on frame[frameSlot].imageAvailable at the required usage scope
    execute frame commands
    signal renderFinished[imageIndex]
    signal frame[frameSlot].completionFence
if submission fails:
    report and enter recovery; do not wait forever on the reset fence

present imageIndex, waiting on renderFinished[imageIndex]
handle presentation result
advance frameSlot
```

`SUBOPTIMAL` acquisition still returns an acquired image; do not simply abandon its synchronization obligations. Per-frame fences can start signaled so the first frame does not wait for nonexistent earlier work.

Resetting a fence before an acquisition that returns early can create a hang: no submission will ever signal the reset fence.

Swapchain recreation and shutdown must satisfy device-work and presentation-resource lifetimes. Do not treat every frame fence as proof that all WSI objects are safe to destroy. [S11] [S29] [S37]

## 14. End-to-end compute: vector addition

Consider:

```text
C[i] = A[i] + B[i], for i in [0, N)
```

No window, surface, swapchain, vertex shader, or fragment shader is required.

### 14.1 Host preparation

1. Select a device with the necessary compute support and memory/limit capabilities.
2. Create buffers for A, B, and C, with required storage and transfer usages.
3. Allocate/bind suitable memory.
4. Upload or initialize A and B, including required host cache management.
5. Compile a compute shader to SPIR-V.
6. Create a descriptor layout/set for the three buffers.
7. Create a pipeline layout containing the descriptor interface and a small count parameter.
8. Create the compute pipeline.

### 14.2 Illustrative GLSL

This is shader source, not a complete runnable Vulkan application:

```glsl
#version 450

layout(local_size_x = 64, local_size_y = 1, local_size_z = 1) in;

layout(std430, set = 0, binding = 0) readonly buffer InputA {
    float a[];
};
layout(std430, set = 0, binding = 1) readonly buffer InputB {
    float b[];
};
layout(std430, set = 0, binding = 2) writeonly buffer OutputC {
    float c[];
};
layout(push_constant) uniform Parameters {
    uint count;
} parameters;

void main() {
    uint i = gl_GlobalInvocationID.x;
    if (i < parameters.count) {
        c[i] = a[i] + b[i];
    }
}
```

### 14.3 Work sizing

For `N = 1000` and local size 64:

```text
workgroups = ceil(1000 / 64) = 16
invocations launched = 16 * 64 = 1024
useful invocations = 1000
guarded extra invocations = 24
```

`vkCmdDispatch(16, 1, 1)` specifies workgroups, not individual threads.

A **workgroup** is not necessarily a hardware wave/subgroup. A 64-invocation workgroup can be executed using different subgroup arrangements on different devices.

Query per-dimension workgroup size, total invocations, dispatch-count limits, and supported subgroup behavior. Use overflow-safe host arithmetic for general problem sizes. Ensure the descriptor ranges actually cover all valid indices; the shader count check does not repair undersized buffer bindings. [S17] [S18]

### 14.4 Submission and result consumption

```text
Record upload copies if required
  -> transfer-write to compute-read dependencies
  -> bind compute pipeline and descriptor sets
  -> supply count
  -> dispatch
  -> dependency for the actual next consumer
  -> submit and track completion
```

There are two different continuations:

```text
GPU consumer:
  compute write -> suitable GPU dependency -> next GPU operation

CPU consumer:
  compute output -> optional readback copy
  -> host-read dependency -> completion wait
  -> non-coherent invalidation if required -> CPU read
```

Do not download an intermediate result merely because one dispatch ended. Keeping intermediates on the GPU can be essential for performance.

For a correctness exercise, set `A[i] = i` and `B[i] = 2*i` for this small range and check `C[i] = 3*i`. Then test non-multiple sizes, repeated dispatches, buffer reuse, and non-coherent paths. Production numerical workloads need explicit accuracy/tolerance and exceptional-value policies. [S10] [S12] [S13] [S17]

## 15. What a Vulkan AI backend actually implements

A neural network is not executed by submitting a model file to the Vulkan loader.

An inference backend typically has to provide:

- Tensor representations, storage layouts, and allocation.
- Operator support and graph partitioning.
- Shader kernels for matrix operations, attention, normalization, activation, copying, and other supported operations.
- Shape-specialized or general pipelines.
- Quantization/dequantization and supported numerical paths.
- Scheduling, synchronization, and temporary-memory reuse.
- Host/device transfer policy.
- CPU fallback or explicit unsupported-operation errors.
- Device capability checks and performance tuning.

```text
Model
  -> inference framework / graph scheduler
  -> Vulkan backend's supported operator implementations
  -> compute pipelines, descriptors, buffers, dispatches
  -> Vulkan driver
  -> GPU
```

For example, llama.cpp's upstream build documentation contains a `GGML_VULKAN` backend option. That is an **application/library backend**, not a replacement Vulkan driver. Building the backend, discovering a GPU, offloading selected operations, and running the entire workload on the GPU are four different facts.

Vulkan on Snapdragon normally means an Adreno GPU path through a suitable Vulkan implementation. It does not automatically use the Hexagon NPU. QNN is a separate AI backend/runtime path. Similarly, Vulkan on an AMD GPU does not automatically use a Ryzen AI NPU.

FP16 arithmetic, 16-bit storage, integer dot products, subgroup operations, and cooperative-matrix features are separate capabilities. The statement "this device supports Vulkan" does not guarantee the precision or kernel features an inference backend needs.

Vulkan portability also does not guarantee parity with CUDA/ROCm libraries, model coverage, tuned kernels, or training support. Compare a specific implementation and workload, not API names. [S05] [S17] [S18] [S36] [S38] [S39]

## 16. Why identical Vulkan code behaves differently across vendors

Correct Vulkan code should obey the same supported API contract, but performance and available features can differ because of:

1. Compiler optimization and register allocation.
2. GPU instruction set and supported data types.
3. Subgroup size and execution behavior.
4. Register/shared-memory capacity and occupancy.
5. Cache hierarchy and memory bandwidth.
6. Dedicated versus unified memory and transfer cost.
7. Graphics tiling and attachment storage behavior.
8. Queue mapping and concurrency.
9. Firmware, scheduling, clocks, thermals, and power limits.
10. Driver bugs, workarounds, and feature coverage.

### AMD example

RADV's ACO compilation, wave arrangement, registers, and command streams affect performance. AMD devices and generations differ; "AMD always uses wave64" is not a valid portability assumption.

### NVIDIA example

NVIDIA's vendor Vulkan driver and Mesa NVK are different implementations. Do not infer their compiler behavior or performance from one another. Familiar CUDA warp terminology is useful background but does not replace Vulkan subgroup capability queries.

### Qualcomm example

Mesa's Adreno documentation describes tile-mode rendering and a system-memory bypass path. Avoiding unnecessary attachment loads/stores can matter significantly. UMA removes some transfer costs but does not make memory free or eliminate cache and synchronization concerns.

A kernel tuned for maximum throughput on a discrete desktop GPU may perform poorly on a mobile SoC. Tune using device properties and measurements, not brand-only branches. [S07] [S18] [S19] [S20] [S21] [S35]

## 17. Designing a production Vulkan backend

The architecture should make ownership and contracts explicit without inventing unnecessary abstraction layers.

| Responsibility | Contract to make explicit |
|---|---|
| Device/capability selection | Required features versus optional optimizations; rejection/fallback reasons |
| Resource management | Allocation, binding, aliasing, usage, lifetime, and retirement |
| Shader/pipeline management | Compilation inputs, interface compatibility, caching, and failure diagnostics |
| Binding management | Descriptor/parameter versions remain valid for in-flight work |
| Command recording | Correct queue-family compatibility and thread ownership |
| Scheduling/synchronization | Producer/consumer dependencies, ownership, and completion tracking |
| Presentation | Surface capabilities, acquisition, presentation, resize, and WSI lifetimes |
| Diagnostics | Identifiable operations, captures, timestamps, logs, and error recovery |

### Important design principles

- Specify the resource-access contract at each pass/operator boundary.
- Track hazards for aliased memory, not only for resource handles.
- Separate resource allocation from the policy for reusing in-flight data.
- Use completion values or equivalent retirement records to defer destruction.
- Make CPU fallback explicit and observable.
- Treat shader compilation failure, missing features, allocation failure, surface loss, and device loss as distinct cases.
- Keep a simple correct execution path before introducing aggressive concurrency.
- Preserve reproducible configuration and workload identifiers in performance records.

A render graph or compute graph can derive dependencies if access declarations are complete and accurate. A graph system cannot infer an undeclared side effect or repair an invalid shader interface by itself.

The principal-engineer question is not just "which class owns this object?" It is also "which event proves the last consumer has finished?" [S01] [S06] [S10] [S11] [S16] [S32]

## 18. Debugging: prove each layer independently

### 18.1 Establish discovery before debugging shaders

On the target system, with Vulkan tools installed, begin with:

```powershell
vulkaninfo --summary
vulkaninfo
vkcube
```

These commands are suggested diagnostics; they were not run against GPU hardware for this report.

- `vulkaninfo` establishes enumerated implementations, devices, and capabilities.
- `vkcube` is a small graphics/presentation smoke test.
- A working cube does not certify your compute shader, extension requirements, memory pressure, or application's synchronization.
- A headless compute service should also have a minimal compute-specific test instead of depending solely on a windowed test.

### 18.2 Record the actual device

Log the selected device, device/driver identifiers where available, API version, enabled features, queue configuration, memory properties, and shader/backend configuration.

A software implementation can return correct output while providing very different performance. Make such fallback visible.

### 18.3 Enable validation during development

Use `VK_LAYER_KHRONOS_validation` where available. Collect messages through appropriate debug-utils integration. Enable synchronization validation and GPU-assisted checks when they are relevant and supported.

Validation reports contain **VUIDs**, identifiers connecting failures to specification rules. Fix the actual violated condition rather than suppressing the message.

Validation-clean does not prove algorithmic correctness or absence of every race. Conversely, measure release performance separately from expensive validation/capture configurations. [S31] [S33]

### 18.4 Inspect the right evidence

| Symptom | First evidence to inspect |
|---|---|
| No devices | Loader discovery, installed ICDs, process architecture, permissions, overrides |
| Wrong device | Application selection policy, device and driver identity |
| Pipeline creation failure | SPIR-V validity, required capabilities, enabled features, pipeline interface |
| Black image | Actual draw execution, attachments, viewport/scissor, bindings, image layouts |
| Incorrect computation | Buffer sizes/offsets/strides, descriptor ranges, numerical logic, dependencies |
| Intermittent corruption | Resource reuse, synchronization, descriptor updates, aliasing, host cache management |
| Hang after resize | Acquisition/presentation result handling, fence reset, swapchain lifetimes |
| Device lost | Validation, device-fault diagnostics if supported, driver/kernel logs, minimal reproduction |
| Unexpected CPU usage | Selected implementation and backend offload/fallback logs |
| Correct but slow | Timelines, GPU timestamps, transfers, barriers, compilation, occupancy, bandwidth |

RenderDoc can inspect command/resource state for supported Vulkan applications you own or are authorized to debug. Vendor profilers expose complementary hardware and scheduling information. A frame capture is not automatically a reliable steady-state performance measurement.

Change one variable at a time: workload, shader, driver, device, or feature path. Keep a known-good baseline. A device fault is not automatically proof of a driver bug; application lifetime and access violations can produce the same symptom. [S19] [S31] [S34]

## 19. Performance engineering

### 19.1 Measure the critical path

Overall latency can involve:

- CPU application and command-recording time.
- Shader/pipeline compilation.
- Allocation and transfer.
- Queue waiting.
- GPU execution.
- Synchronization.
- Readback or presentation waiting.

These can overlap. End-to-end latency is the critical path through the dependency graph, not always the sum of independently measured durations.

Measure cold startup separately from warm steady state. Use GPU timestamps with the device's supported query behavior and timestamp properties. Do not use CPU submission duration as a proxy for GPU execution time.

### 19.2 Know the limiting resource

A useful idealized lower-bound model is:

```text
kernel time >= max(
    required memory traffic / effective bandwidth,
    required arithmetic / effective compute throughput
)
```

Launch, synchronization, transfer, latency, and scheduling overheads sit outside that simplified model.

Vector addition has little arithmetic per byte transferred. Matrix multiplication can reuse data much more heavily. These workloads need different tuning strategies.

### 19.3 Optimization order

1. Remove accidental CPU fallback and unnecessary transfers.
2. Remove per-operation global idle waits and avoid excessive submission overhead.
3. Reuse pipelines/resources safely; reduce compilation stalls.
4. Fix memory layout and access patterns.
5. Tune workgroup size, register pressure, shared-memory use, and occupancy.
6. Introduce overlap/multiple queues only where traces show an opportunity.
7. Add specialized precision or subgroup paths behind capability checks.
8. Revalidate correctness and end-to-end latency after every optimization.

High utilization alone does not prove good performance. Occupancy is a constraint and diagnostic, not a universal metric to maximize. Extra queues can increase contention; larger batches can improve throughput while violating latency requirements. [S06] [S07] [S16] [S18] [S19] [S21]

## 20. Deployment, portability, and advanced features

### What must be deployed or present

- Correct application architecture and dependencies.
- A usable Vulkan loader.
- Compatible driver implementation and kernel/firmware stack.
- Appropriate device permissions and presentation integration where needed.
- Shader artifacts for the required Vulkan/SPIR-V environment.
- Correct optional-layer configuration for the environment.
- Explicit driver/device/feature selection and useful failure messages.

The Vulkan SDK is a development package. Installing newer headers or tools does not upgrade a GPU's capabilities. A container can carry user-space dependencies, but it does not replace the host kernel driver, firmware, permissions, or device-access configuration.

### Advanced families built on the same foundations

| Family | Additional concern |
|---|---|
| Ray tracing | Acceleration structures, shader stages, build/trace dependencies, feature support |
| Mesh shading | Different geometry pipeline and device limits |
| Vulkan Video | Codec-specific capabilities, profiles, resources, and queue support |
| Sparse resources | Residency/binding dependencies and memory management |
| External memory/semaphores | Cross-API/process handle compatibility, ownership, and synchronization |
| Device groups | Explicit multi-device capabilities and resource/execution policy |
| Descriptor indexing/buffers | Binding model, limits, update/lifetime rules |
| Portability implementations | Supported subset and portability enumeration/feature rules |

For example, sharing memory with CUDA or another API requires an explicitly supported interop path. Two APIs addressing the same GPU does not make their allocations or synchronization objects automatically interchangeable.

Performance portability means preserving acceptable performance through capability-aware implementations and measurement. It is a stronger requirement than compiling the same source code everywhere.

Keep a tested matrix of **device + driver + OS/kernel + application build + enabled features + workload**. Neither an API version nor a vendor name is an adequate substitute. [S03] [S04] [S05] [S28] [S30] [S35]

## 21. Misconceptions to eliminate

| Misconception | Correct model |
|---|---|
| Mesa -> Vulkan -> OpenGL -> OpenCL is the pipeline | They are projects/APIs at different layers; translation is an explicit optional design |
| Mesa is the Linux kernel driver | Mesa implementations are principally user-space software; kernel drivers are separate |
| Every Mesa driver uses Gallium and LLVM | Mesa contains different driver architectures and compiler backends |
| A Vulkan backend is a driver | It might instead be an engine, translation, compute, or compiler backend |
| Vulkan only renders graphics | It also supports compute and other enabled capabilities |
| Finding Vulkan proves GPU execution | A software Vulkan implementation can expose a CPU device |
| A dispatch runs when recorded | Execution requires submission and later scheduling |
| Same queue means every resource access is synchronized | Correct dependencies are still required |
| Unified/coherent memory means no synchronization | Visibility properties and execution/lifetime rules are distinct |
| More queues always means more GPU engines | Queue-to-hardware mapping is implementation-defined |
| A workgroup is always a warp/wave | Workgroups and subgroups are different concepts |
| SPIR-V is hardware machine code | The driver normally compiles or lowers it to a target ISA |
| A frame fence means presentation is finished | Presentation synchronization has separate lifetime requirements |
| Vulkan on Snapdragon automatically uses the NPU | A Vulkan GPU path and a QNN NPU path are distinct |
| One successful frame certifies the backend | Correctness, concurrency, lifecycle, memory pressure, and performance need separate tests |

## 22. A practical learning and qualification sequence

| Stage | Build or inspect | Evidence required before proceeding |
|---|---|---|
| 1. Discovery | Instance, enumeration, capability report | Correct device/driver selected; required features verified |
| 2. Compute basics | Vector addition and readback | Correct output for boundary sizes; clean relevant validation |
| 3. Memory | Staging, host-visible paths, repeated reuse | Correct dependencies and non-coherent cache management |
| 4. Graphics | A triangle or simple render | Correct image, surface, resize, and presentation handling |
| 5. In-flight execution | Multiple frame/work slots | No premature buffer, descriptor, command, or semaphore reuse |
| 6. Shader understanding | Inspect SPIR-V and pipeline behavior | Understand interfaces, specialization, compilation, and caching |
| 7. Cross-device testing | NVIDIA, AMD, Qualcomm targets in scope | Explicit capability paths; correct outputs on each supported combination |
| 8. Performance | Fixed workloads and timelines | Separate cold/warm results; latency/throughput/memory/power goals met |
| 9. Production robustness | Errors, device loss, memory pressure, deployment | Actionable diagnostics and tested recovery/rejection policies |

A useful initial compute boundary set is `N = 1, 63, 64, 65, 999, 1000, 1001`, plus the application's defined empty-input behavior. Add repeated runs, data changes between submissions, and overlapping work only after the single-submission path is correct.

For graphics, test minimization, resizing, differing swapchain image counts, multiple frames in flight, and surface recreation. Exercise a different queue-family arrangement if the production target uses one.

For inference, qualify operator coverage, numerical accuracy, actual offload, model initialization, memory footprint, prefill/decode behavior where relevant, and sustained rather than short-burst performance.

## 23. Compact glossary

| Term | Meaning |
|---|---|
| API | Public interface and behavioral contract |
| ABI | Binary-level calling/layout contract between compiled components |
| ICD | Installable Client Driver |
| UMD / KMD | User-mode driver / kernel-mode driver |
| WSI | Window System Integration |
| WDDM | Windows Display Driver Model |
| DRM | Linux Direct Rendering Manager; not digital-rights management in this context |
| RHI | Render Hardware Interface, an engine-level abstraction |
| IR / ISA | Intermediate representation / instruction set architecture |
| SPIR-V | Binary shader/program intermediate representation |
| NIR | Mesa's shared shader intermediate representation |
| ACO / NAK / ir3 | Compiler components associated with particular Mesa GPU paths |
| Descriptor | Shader-visible resource binding description |
| Pipeline | Executable shader/state configuration |
| Dispatch | Launch of compute workgroups |
| Invocation | One logical execution of a shader |
| Workgroup | Application-defined group of compute invocations |
| Subgroup | Group of invocations supporting the device's subgroup operations |
| Occupancy | How much execution work can be resident, subject to hardware resources |
| Barrier | Scoped execution/memory dependency mechanism |
| RAW / WAR / WAW | Read-after-write / write-after-read / write-after-write hazards |
| UMA | Unified Memory Architecture |
| Staging buffer | Intermediate resource used for transfers |
| Residency | Whether resource storage is available in the required memory system at execution |
| Swapchain | Presentation image-management mechanism |
| Frames in flight | Application work/resource sets allowed to remain outstanding |
| VUID | Vulkan valid-usage identifier |
| Device loss | Failure state reported when the logical device can no longer continue normally |

## 24. Sources and verification limits

The guide is original explanatory text grounded in the following primary sources. Sources were inspected on **17 October 2026**, including sources inspected for the preceding vendor-stack comparison in this conversation.

**Limits:** no target GPU was interrogated, no driver was installed, no shader was compiled or executed, and no comparative performance claim was measured. Code is instructional, not a complete implementation. Source pages and repository default branches can contain changing or historical material; use the exact specification version and supported driver release for production decisions. Proprietary compiler internals are not inferred from Mesa.

- [S01] Vulkan specification: fundamentals, object use, and host synchronization.
- [S02] Vulkan Guide: what Vulkan is.
- [S03] Khronos loader interface architecture.
- [S04] Khronos loader driver discovery, manifests, and overrides.
- [S05] Querying extensions and features.
- [S06] Vulkan queue semantics and implementation-defined hardware mapping.
- [S07] Memory allocation, discrete GPUs, and UMA.
- [S08] Shader memory layout.
- [S09] Synchronization overview.
- [S10] Khronos synchronization examples, including upload and CPU readback.
- [S11] Safe swapchain presentation-semaphore reuse.
- [S12] `vkFlushMappedMemoryRanges` specification.
- [S13] `vkInvalidateMappedMemoryRanges` specification.
- [S14] SPIR-V and Vulkan.
- [S15] High-level shader language comparison.
- [S16] Pipeline caching.
- [S17] Compute shaders, invocations, and dispatch sizing.
- [S18] Subgroups and subgroup-size control.
- [S19] Mesa RADV architecture, command streams, and ACO compilation.
- [S20] Mesa NVK and NAK.
- [S21] Mesa Freedreno/Turnip and Adreno architecture.
- [S22] Mesa ir3 compiler notes.
- [S23] Mesa Zink and its underlying Vulkan requirements.
- [S24] Mesa LLVMpipe.
- [S25] DXVK project.
- [S26] vkd3d-proton project.
- [S27] ANGLE project.
- [S28] MoltenVK project and current platform/deprecation guidance.
- [S29] Window System Integration.
- [S30] Microsoft WDDM architecture.
- [S31] Vulkan validation overview.
- [S32] Vulkan Memory Allocator.
- [S33] Khronos Vulkan Tools.
- [S34] RenderDoc.
- [S35] NVIDIA Vulkan driver support.
- [S36] llama.cpp build documentation, Vulkan backend section.
- [S37] Khronos rendering and presentation tutorial.
- [S38] ONNX Runtime QNN execution provider.
- [S39] AMD Ryzen AI Windows ML tutorial and NPU path.

[S01]: https://docs.vulkan.org/spec/latest/chapters/fundamentals.html
[S02]: https://docs.vulkan.org/guide/latest/what_is_vulkan.html
[S03]: https://github.com/KhronosGroup/Vulkan-Loader/blob/main/docs/LoaderInterfaceArchitecture.md
[S04]: https://github.com/KhronosGroup/Vulkan-Loader/blob/main/docs/LoaderDriverInterface.md
[S05]: https://docs.vulkan.org/guide/latest/querying_extensions_features.html
[S06]: https://docs.vulkan.org/guide/latest/queues.html
[S07]: https://docs.vulkan.org/guide/latest/memory_allocation.html
[S08]: https://docs.vulkan.org/guide/latest/shader_memory_layout.html
[S09]: https://docs.vulkan.org/guide/latest/synchronization.html
[S10]: https://github.com/KhronosGroup/Vulkan-Guide/blob/main/chapters/synchronization_examples.adoc
[S11]: https://docs.vulkan.org/guide/latest/swapchain_semaphore_reuse.html
[S12]: https://docs.vulkan.org/refpages/latest/refpages/source/vkFlushMappedMemoryRanges.html
[S13]: https://docs.vulkan.org/refpages/latest/refpages/source/vkInvalidateMappedMemoryRanges.html
[S14]: https://docs.vulkan.org/guide/latest/what_is_spirv.html
[S15]: https://docs.vulkan.org/guide/latest/high_level_shader_language_comparison.html
[S16]: https://docs.vulkan.org/guide/latest/pipeline_cache.html
[S17]: https://docs.vulkan.org/guide/latest/compute_shaders.html
[S18]: https://docs.vulkan.org/guide/latest/subgroups.html
[S19]: https://docs.mesa3d.org/drivers/radv.html
[S20]: https://docs.mesa3d.org/drivers/nvk.html
[S21]: https://docs.mesa3d.org/drivers/freedreno.html
[S22]: https://docs.mesa3d.org/drivers/freedreno/ir3-notes.html
[S23]: https://docs.mesa3d.org/drivers/zink.html
[S24]: https://docs.mesa3d.org/drivers/llvmpipe.html
[S25]: https://github.com/doitsujin/dxvk
[S26]: https://github.com/HansKristian-Work/vkd3d-proton
[S27]: https://chromium.googlesource.com/angle/angle/+/main/README.md
[S28]: https://github.com/KhronosGroup/MoltenVK
[S29]: https://docs.vulkan.org/guide/latest/wsi.html
[S30]: https://learn.microsoft.com/en-us/windows-hardware/drivers/display/windows-vista-and-later-display-driver-model-architecture
[S31]: https://docs.vulkan.org/guide/latest/validation_overview.html
[S32]: https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator
[S33]: https://github.com/KhronosGroup/Vulkan-Tools
[S34]: https://github.com/baldurk/renderdoc
[S35]: https://developer.nvidia.com/vulkan-driver
[S36]: https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md#vulkan
[S37]: https://docs.vulkan.org/tutorial/latest/03_Drawing_a_triangle/03_Drawing/02_Rendering_and_presentation.html
[S38]: https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html
[S39]: https://github.com/amd/RyzenAI-SW/blob/main/WinML/README.md
