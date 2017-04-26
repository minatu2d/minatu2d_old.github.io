# Hướng dẫn sử dụng Kit phát triển phần mềm (SDK) của Yocto Project dành cho Developer

### Scott Rifenbark

Scotty's Documentation Services, LLC

`<[srifenbark@gmail.com](mailto:srifenbark@gmail.com)>`

Copyright © 2010-2016 Linux Foundation

Permission is granted to copy, distribute and/or modify this document under
the terms of the [Creative Commons Attribution-Share Alike 2.0 UK: England &
Wales](http://creativecommons.org/licenses/by-sa/2.0/uk/) as published by
Creative Commons.

### Note

For the latest version of this manual associated with this Yocto Project
release, see the [Yocto Project Software Development Kit (SDK) Developer's
Guide](http://www.yoctoproject.org/docs/2.2/sdk-manual/sdk-manual.html) from
the Yocto Project website.

**Revision History**

Revision 2.1

April 2016

Released with the Yocto Project 2.1 Release.

Revision 2.2

October 2016

Released with the Yocto Project 2.2 Release.

* * *

**Mục lục**

1. Giới thiệu

1.1. Giới thiệu

1.1.1. Về Cross-Development Toolchain

1.1.2. Về Sysroots

1.1.3. Về QEMU Emulator

1.1.4. Về Yocto Plug-in dành cho IDE Eclipse

1.1.5. Về các tool cho việc nâng cao hiệu năng (Performance Enhancing Tools)

1.2. Về mô hình phát triển SDK (SDK Development Model)


2. Sử dụng SDK mở rộng (Extensible SDK)

2.1. Tại sao lại sử dụng Extensible SDK và có gì bên trong nó?

2.2. Thiết lập để sử dụng Extensible SDK

2.3. Chạy script Setup môi trường cho Extensible SDK

2.4. Sử dụng `devtool` trong SDK của bạn

2.4.1. Sử dụng `devtool add` để thêm ứng dụng

2.4.2. Sử dụng `devtool modify` để sửa source của một component sẵn có (Existing Component)

2.4.3. Sử dụng `devtool upgrade` để tạo một phiên bản của một Recipe để support
một phiên bản mới của phần mềm

2.5. Một cái nhìn gần hơn đối với `devtool add`

2.5.1. Tên và phiên bản

2.5.2. Phát hiện phụ thuộc và Mapping

2.5.3. Phát hiện licence

2.5.4. Thêm phần mềm chỉ có Makefile-Only

2.5.5. Thêm các công cụ Native

2.5.6. Thêm các module Node.js Modules

2.6. Làm việc với các Recipes

2.6.1. Tìm Logs và Work Files

2.6.2. Thiết lập các tham số cấu hình

2.6.3. Chia sẻ file giữa các Recipes

2.6.4. Đóng gói phần mềm

2.7. Phục hồi Target Device về trạng thái ban đầu của nó

2.8. Cài đặt thêm Items vào Extensible SDK

2.9. Update Extensible SDK

2.10. Tạo một SDK kế thừa với những Components khác

3. Sử dụng một SDK chuẩn



3.1. Tại sao sử dụng một Standard SDK và có gì trong nó?

3.2. Cài đặt SDK

3.3. Chạy script thiết lập môi trường SDK

4. Sử dụng trực tiếp SDK Toolchain



4.1. Các project dựa trên Autotools-Based Projects



4.1.1. Tạo và chạy một project dựa trên dựa trên GNU Autotools

4.1.2. Truyền các options ở phía Host

4.2. Các project dựa trên Makefile-Based Projects

4.3. Phát triển ứng dụng trên Eclipse™


4.3.1. Workflow khi sử dụng Eclipse™

4.3.2. Working bên trong Eclipse

A. Hiểu vể SDK


A.1. Xác định ví trí của bộ cài đặt Pre-Built SDK

A.2. Về việc build một SDK Installer

A.3. Giải nén hệ thống fileRoot Filesystem

A.4. Cấu trúc thư mục của Standard SDK khi được cài đặt

A.5. Cấu trúc thư mục của Extensible SDK khi được cài đặt

B. Tùy biến Extensible SDK


B.1. Cấu hình Extensible SDK

B.2. Điều chỉnh Extensible SDK để phù hợp với setup trên hệ thống build

B.3. Thay đổi diện mạo của Extensible SDK

B.4. Cung cấp các bản cập nhật sau khi đã cài đặt Extensible SDK

B.5. Cung cấp các nội dung có thể cài đặt được cho Extensible SDK

B.6. Tối ưu kích thước của bộ cài đặt Extensible SDK dành cho việc tải về

C. Tùy chỉnh Standard SDK

C.1. Thêm các gói riêng biệt vào Standard SDK

C.2. Thêm tài liệu về API cho Standard SDK

D. Sử dụng Eclipse Mars

D.1. Thiết lập cho phiển bản Mars của the Eclipse IDE


D.1.1. Cài đặt Eclipse IDE phiên bản Mars

D.1.2. Cấu hình Eclipse IDE phiển bản Mars

D.1.3. Cài đặt và sử dụng Yocto Plug-in trên Eclipse Mars

D.1.4. Cấu hình Yocto Plug-in trên Eclipse Mars 

D.2. Tạo project

D.3. Cấu hình Cross-Toolchains

D.4. Build Project

D.5. Khởi động QEMU ở chế độ User-Space NFS

D.6. Triển khai và Debugging ứng dụng

D.7. Sử dụng Linuxtools

## Chương 1. Giới thiệu

**Mục lục**

1.1. Giới thiệu

1.1.1. Về Cross-Development Toolchain

1.1.2. Về Sysroots

1.1.3. Về QEMU Emulator

1.1.4. Về Yocto Plug-in cho Eclipse

1.1.5. Các tool năng cao hiệu năng (Performance Enhancing Tools)

1.2. Mô hình phát triển SDK

## 1.1. Giới thiệu

Chào mừng bạn đến với hướng dẫn về Kit phát triển phần mềm (SDK) của Yocto Project dành cho Developer.
Hướng dẫn này cung cấp những thông tin giải thích việc làm thế nào để sử dụng cả SDK mở rộng (extensible SDK) và SDK chuẩn (standard SDKs) của Yocto Project để phát triển ứng dụng và tạo ảnh hệ thống.
Ngoài ra, tài liệu này cũng cung cấp thông tin về việc làm thế nào để sử dụng Eclipse™ IDE kết hợp với SDK trong quá trình phát triển ứng dụng.

### Ghi chú

Tính đến phiên bản 2.0 của Yocto Project, việc phát triển ứng dụng được thực hiện thông qua Application Development Toolkit (ADT), các cross-development toolchains chạy độc lập và các công cụ khác.
Từ phiên bản 2,1 của Yocto Project, việc phát triển ứng dụng được chuyển sang extensible SDK với rất nhiều tiện ích và một SDK chuẩn (standard SDK) gần với công cụ cũ.

Mỗi SDK sẽ bao gồm các thành phần sau:

  * _Cross-Development Toolchain_: Toolchain chứa một compiler, một debugger, và rất nhiều công cụ linh tinh khác.

  * _Libraries, Headers, and Symbols_: Thư viện dạng binary, các file header, và các symbols(hàm, biến toàn cục)
 được có liên quan đến một ảnh hệ thống cụ thể ( ví dụ: chúng phải cùng phiên bản với image chẳng hạn).

  * _Environment Setup Script_: Các file `*.sh`, một khi được chạy, chúng sẽ thiết lập môi trường cross-development bằng cách định nghĩa các biến môi trường cũng như chuẩn bị cho việc sử dụng SDK.

 Ngoài ra, một SDK mở rộng (extensible SDK) có những công cụ cho phép bạn dễ dàng thêm ứng dụng mới, các thư viện vào ảnh hệ thống, chỉnh sửa mã nguồn của component sẵn có, test các thay đổi trên phần cứng, và dễ dàng tích hợp ứng dụng vào [OpenEmbedded build system](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#build-system-term).

 Bạn có thể sử dụng SDK một cách độc lập để phát triển và test code, cái mà cuối cùng sẽ được chạy trên phần cứng đích (target machine).
 Các SDKs thông thường là hoàn toàn không có phụ thuộc (self-contained), tức là nó chứa tất cả những gì cần thiết rồi.
Các binaries tạo ra sẽ được linked với một bản copy của `libc`, vì thế chúng không cần bất kì phụ thuộc nào từ máy đích nữa.
Để làm được điều này, đường đẫn dành cho bộ load động (dynamic loader) được cấu hình tại thời điểm cài đặt không thể bị thay đổi tùy tiện được. Đây là lý do có một wrapper cho `populate_sdk` và `populate_sdk_ext`.

 Một đặc điểm khác của các SDKs, nó là tập các cross-compiler toolchain ở dạng binaries chỉ sinh code cho một architecture nhất định mà thôi.
 Đặc điểm này sẽ tạo thuận lợi trong thực tế khi trên phần cứng ta sử dụng `gcc` không phải là một câu lệnh đơn mà là một compiler với các option được thiết lập sẵn. Những option này được set bởi script thiết lập môi trường (environment script) và được lưu vào một biến môi trường gọi là [`CC`](http://www.yoctoproject.org/docs/2.2
/ref-manual/ref-manual.html#var-CC) dành cho compiler và [`LD`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-LD) dành cho Linker. Điều này sẽ giảm không gian cần thiết cho các công cụ.
 Hiểu là như vậy, nhưng, vẫn cần một sysroot cho mỗi target muốn build vì các binaries nằm trên đó là phụ thuộc target.

 Mỗi trường phát triển bằng SDK (SDK development environment) chứa những thành phần sau:

  * Một SDK không phụ thuộc (self-contained SDK), là một bộ bao gồm một cross-toolchain cho một kiến trúc cụ thể và sysroots đồng bộ với nó (trên target và native), cả 2 được build bởi hệ thống build OpenEmbedded (ví dụ: SDK). Toolchain và sysroot có gì, được build như thế nào thì được quy định bởi các [Metadata](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#metadata) chứa cấu hình và thành phần mở rộng, SDK cho phép bạn phát triển chéo (cross-develop) ứng dụng trên máy host rồi chạy trên phần cứng target ( target hardware). Ngoài ra, SDK mở rộng chứa một số công cụ tiện ích gọi là `devtool` nữa.

  * The Quick EMUlator (QEMU), cho phép bạn giả lập phần cứng đích (target hardware). QEMU không phải là một phần của SDK. Bạn phải build và thêm Emulator này riêng. Tuy nhiên, QEMU đóng một vai trò quan trọng trong quá trình phát triển có sử dụng SDK.

  * Yocto Plug-in cho IDE Eclipse. Plug-in này đã sẵn có cho bạn sử dụng nếu bạn là một người sử dụng IDE Eclipse. Cũng giống với QEMU, Plug-in này vốn không phải là một phần của SDK, nó được sử dụng trong quá trình phát triển thì đúng hơn.

  * Rất nhiều công cụ liên quan đến việc đánh giá hiệu năng [tools](http://www.eclipse.org/linuxtools/index.php) cái sẽ hộ trợ rất nhiều trong quá trình phát triển. Những công cụ này cũng được tách biệt với phần thực sự của SDK nhưng có thể được đưa vào sử dụng trong quá trình phát triển.

 Tóm lại, SDK mở rộng và SDK chuẩn (extensible and standard SDK) có rất nhiều tính năng chung. Tuy nhiên, SDK mở rộng có nhiều công cụ phát triển mạnh giúp bạn làm việc nhanh hơn trong quá trình phát triển ứng dụng. Bên dưới là một bảng tổng kết những sự khác nhau chính giữa SDK chuẩn và SDK mở rộng khi xem xét để build:

<Được nhúng vào bằng HTML>

### 1.1.1. Về Cross-Development Toolchain

[Cross-Development Toolchain](http://www.yoctoproject.org/docs/2.2/dev-
manual/dev-manual.html#cross-development-toolchain) chứa một cross-compiler, một cross-linker, và một cross-debugger được sử dụng để phát triển ứng dụng phía user-space cho phần cứng đích (targeted hardware). Ngoài ra, trong SDK mở rộng (extensible SDK), còn có một bộ công cụ gọi là `devtool`.
 Các toolchain được đặt cùng với SDK bằng script cài đặt thông qua [Build Directory](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#build-directory) cái được tạo ra từ Metadata cấu hình hoặc hoặc mở rộng cho thiết bị đích (targeted device). Các cross-toolchain chỉ làm việc với target sysroot phù hợp.

### 1.1.2. Về Sysroots (Filesystem của root)

Sysroot native và target chứa các file headers and thư viện (libraries) sử dụng cho việc sinh mã binary chạy trên kiến trúc đích (target architecture). Sysroot target là hệ thống file ở root mà target sử dụng và được build bởi hệ thống build OpenEmbedded, sử dụng cùng một tập các Metadata configuration để build toolchain.

### 1.1.3. Về QEMU Emulator

QEMU emulator cho phép bạn giả lập phần cứng hardware để chạy ứng dụng hoặc ảnh hệ thống. QEMU không phải là một phần của SDK, chúng được đưa vào sử dụng theo các dạng như sau:

  * Nếu bạn clone Git repository `poky` trong lúc tạo [Source Directory](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#source-directory) và bạn đã chạy script setup môi trường rồi, thì QEMU đã được cài đặt và có thể sử dụng.

  * Bạn tải một phiên bản của Yocto Project giải nén rồi tạo một thư mục [Source Directory](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#source-directory) và bạn cũng đã chạy script setup môi trường rồi, thì QEMU sẽ được cài đặt và có thể sử dụng được.

  * Nếu bạn cài đặt từ file nén tarball chứa cross-toolchain và bạn đã chạy script thiết lập cho toolchain rồi, thì QEMU sẽ được cài đặt và có thể sử dụng được ngay.

### 1.1.4. Eclipse Yocto Plug-in

The Eclipse IDE is a popular development environment and it fully supports
development using the Yocto Project. When you install and configure the
Eclipse Yocto Project Plug-in into the Eclipse IDE, you maximize your Yocto
Project experience. Installing and configuring the Plug-in results in an
environment that has extensions specifically designed to let you more easily
develop software. These extensions allow for cross-compilation, deployment,
and execution of your output into a QEMU emulation session. You can also
perform cross-debugging and profiling. The environment also supports many
performance-related [tools](http://www.eclipse.org/linuxtools/index.php) that
enhance your development experience.

### Ghi chú

 Phiên bản trước của Yocto Plug-in cho Eclipse có các tool chạy ở user-space ("user-space tools")
( ví dụ: LatencyTOP, PowerTOP, Perf, SystemTap, and Lttng-ust) đã được thêm vào để sử dụng trong quá trình phát triển. Nhưng tool này không còn được sử dụng từ phiên bản này của Plug-in.

 Về chi tiết cho quá trình phát triển ứng dụng sử dụng IDE Eclipse cũng như chi tiết ví dụ làm thế nào để
cài đặt, cấu hình Yocto Project Plug-in cho Eclipse, xem thêm ở chương "Developing Applications Using Eclipse™".

### 1.1.5. Các tool đánh giá hiệu năng (Performance Enhancing Tools)

 Có rất nhiều tool mà IDE Eclipse hỗ trợ, cho phép bạn đánh giá,
debug, và thực hiện các bước truy vết khi phát triển ứng dụng sử dụng Eclipse.
Thông tin về các tool này, có thể xem tại [http://www.eclipse.org/linuxtools/](http://www.eclipse.org/linuxtools/).

## 1.2. Mô hình phát triển sử dụng SDK (SDK Development Model)

 Về nguyên tắc, các SDK sẽ phù hợp với quá trình phát triển như sau:

![](figures/sdk-environment.png)

SDK có thể được cài đặt ở bất cứ máy nào và có thể được sử dụng để phát triển ứng dụng,
 ảnh hệ thống, và cả kernel nữa. Một SDK thậm chí có thể được sử dụng bởi QA Enginer
 hoặc Release Engineer nữa. Khái niệm nền tảng ở đây là máy mà SDK được cài đặt
 không cần có bất cứ liên quan gì với máy mà Yocto Project được cài đặt.
 Developer hoàn toàn có thể biên dịch, test các trên máy của họ, 
 sau đó, khi code đã ngon lành rồi, thì họ mang code đó đến máy cài đặt Yocto
Project. Khi đã có code, thư viện rồi , ảnh hệ thống có thể được build lại. 

 Bạn đơn giản cần làm theo các bước như sau:

  1. _Cài đặt SDK tương ứng với phần cứng đích của bạn (target hardware):_ 
 Về cách cài đặt, hãy xem ở chương "Installing the SDK".

  2. _ Tải hoặc là build ảnh hệ thống đích (Target Image):_ 
Yocto Project hỗ trợ một vài kiến trúc đích (target architectures) 
 và cũng có rất nhiều ảnh kernel, root filesystem.

 Nếu ban đang có ý định phát triển ứng dụng cho phần cứng hardware, hãy xem qua phần [`machines
`](http://downloads.yoctoproject.org/releases/yocto/yocto-2.2/machines)
 ở chỗ Tải về chọn máy đích (target machine) sau đó tải ảnh kernel và root filesystem.
 Ở khu vực Tải về đó cũng có một vài file hỗ trợ một vài phần cứng nhất định. 
 Ví dụ, file đuôi `.hddimg` và kết hợp giữa kernel image với filesystem, boot loaders trong 1 file.
 Chắc chắn rằng bạn tải đúng file cho quá trình phát triển cụ thể của bạn.

 Nếu bạn định phát triển ứng dụng chạy và test sử dụng QEMU emulator, 
 hãy vào mục [`machines/qemu`](http://downloads.yoctoproject.o
rg/releases/yocto/yocto-2.2/machines/qemu) ở khu vực tải về. 
Từ đó vào thư mục tương ứng với kiến trúc đích của bạn ( ví dụ: `qemux86_64` dành cho
 kiến trúc dựa trên Intel®-based 64-bit). 
 Tải kernel, root filesystem, và bất cứ file nào khác cần cho quá trình phát triển của bạn.

### Ghi chú 

 Để sử dụng root filesystem trong QEMU, bạn cần giải nén nó. Xem chương về 
"Extracting the Root Filesystem" để biết cách giải nén một root file system. 

  3. _ Phát triển và test ứng dụng:_ Ở thời điểm này, chúng ta có tất cả các tool để phát triển ứng dụng, bao gồm cả QEMU. Nếu bạn muốn tách riêng phần cài đặt và sử dụng QEMU emulator, bạn có thể vào trang chủ [QEMU Home Page](http://wiki.qemu.org/Main_Page) để tải về cũng như học cách sử dụng emulator này.
Xem thêm ở chương "[Using the Quick EMUlator (QEMU)](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#dev-manual-qemu)" trong hướng dẫn phát triển Yocto Project về việc sử dụng QEMU trong Yocto Project.

 Phần còn lại của tài liệu này sẽ mô tả cách làm thế nào để sử dụng SDK chuẩn (standard SDK) và 
SDK mở rộng (extensible SDK). Thông tin trong phần phụ lục cũng miêu tả cách build, cài đặt, chỉnh sửa một SDK.

## Chương 2. Sử dụng SDK mở rộng 

**Mục lục**

2.1. Tại sao lại sử dụng SDK mở rộng và có gì bên trong nó?

2.2. Thiết lập để sử dụng SDK mở rộng 

2.3. Chạy script thiết lập môi trường cho SDK mở rộng

2.4. Sử dụng `devtool` trong SDK của bạn 

    

2.4.1. Sử dụng `devtool add` để thêm ứng dụng

2.4.2. Sử dụng `devtool modify` để sửa source và component có sẵn 

2.4.3. Sử dụng `devtool upgrade` để tạo một phiên bản của Recipe cái hỗ trợ
phiên bản mới hơn của phần mềm

2.5. Một cái nhìn gần hơn về `devtool add`

    

2.5.1. Tên và phiên bản 

2.5.2. Phát hiện phục thuộc và Mapping

2.5.3. Phát hiện licence 

2.5.4. Thêm phần mềm chỉ hỗ trợ build bằng (Makefile-Only Software)

2.5.5. Thêm các tool Native

2.5.6. Thêm module của Node.js

2.6. Làm việc với các Recipe 

    

2.6.1. Tìm log và các work file 

2.6.2. Thiết lập các tham số cấu hình 

2.6.3. Chia sẻ file giữa các recipe 

2.6.4. Đóng gói 

2.7. Phục hồi máy target (target device) về trạng thái ban đầu 

2.8. Cài đặt thêm cho SDK mở rộng 

2.9. Update cho SDK mở rộng 

2.10. Tạo một bản SDK kế thừa với những item được thêm vào 

 Chương này sẽ nói về SDK mở rộng, rồi làm thế nào để cài đặt nó. 
Thông tin sẽ về SDK bao gồm làm thế nào để cài đặt nó, đưa ra cái nhìn 
về chắc năng của `devtool`. SDK mở rộng kiến việc thêm một ứng dụng mới 
thư viện vào ảnh hệ thống, hay sửa source của một component có sẽ 
rồi test trên phần cứng đích trở nên dễ dàng hơn, và nó cũng cho phép
dễ dàng tích hợp vào [OpenEmbedded build system](http://www.yoctoproject.org/docs/2.2
/dev-manual/dev-manual.html#build-system-term) nữa.

### Ghi chú 

 Để xem so sánh chi tiết giữa tính năng của SDK mở rộng và SDK chuẩn
hãy xem ở chương "Introduction".

 Ngoài chức năng `devtool` được thêm vào SDK mở rộng, bạn vẫn có thể sử dụng
trực tiếp toolchain, ví dụ cho Makefile, Autotools, và project được tạo bởi Eclipse.
 Xem thêm chương "Using the SDK Toolchain Directly".

## 2.1. Tại sao lại sử dụng SDK mở rộng và có gì trong nó

SDK mở rộng cung cấp môi trường bao gồm cross-development toolchain và libraries
 được điều chỉnh cho một ảnh hệ thống cụ thể. Bạn sẽ sử dụng SDK mở rộng nếu
 bạn muốn một toolchain kèm theo một tập các công cụ được thiết kế cho môi trường phát triển của Yocto Project.

 SDK mở rộng sau khi được cài đặt sẽ chứa một vài files và thư mục.
 Về cơ bản, nó sẽ có một script để setup môi trường phát triển, các file cấu hình,
một hệ thống build bên trong, và bộ công cụ `devtool`.

## 2.2. Thiết lập để sử dụng SDK mở rộng

 Đầu tiên, bạn cần cài đặt  SDK trên máy phát triển bằng cách chạy script cài đặt có 
phần mở rộng `*.sh`.

 Bạn có thể tải định dạng nén tarball của bộ cài đặt, cái đã bao gồm toolchain bên trong,
 scrip để chạy QEMU có tên là `runqemu`, một hệ thống build bên trong, `devtool`, và các file hỗ trợ 
 từ thư mục phù hợp nằm ở [http://downloads.yoctoproject.org/releas
es/yocto/yocto-2.2/toolchain/](http://downloads.yoctoproject.org/releases/yoct
o/yocto-2.2/toolchain/). Toolchains có dạng binary cho cả môi trường phát triển 32-bit và 64-bit x86
 lần lượt trong các thư mục `i686` and `x86_64`.
Toolchain mà Yocto Project cung cấp dựa trên ảnh hệ thống `core-image-sato`
 và chứa các thư viện (libraries) tương ứng với việc phát triển ứng dụng trên ảnh này.
 Mỗi loại của môi trường phát triển thường hỗ trợ từ 5 phần cứng đích trở lên. 

 Tên file nén tarball của bộ cài đặt thường bắt đầu bằng hệ thống host mà nó chạy, tiếp theo đó là
kiến trúc đích mà nó hỗ trợ. Một SDK mở rộng có thêm phần "-ext" trong tên.

    
    
         poky-glibc-_host_system_-_image_type_-_arch_-toolchain-ext-_release_version_.sh
    
         Trong đó:
             _host_system_ là một chuỗi miêu tả hệ thống host để chạy SDK:
    
                        i686 or x86_64.
    
             _image_type_ là ảnh mà SDK đã được build trên đó.
    
             _arch_  là một chuỗi mô tả kiến trúc hay chính là kiến trúc đích, bao gồm:
    
                        i586, x86_64, powerpc, mips, armv7a or armv5te
    
             _release_version_ là một chuỗi miêu tả số phiên bản của Yocto Project:
    
                        2.2, 2.2+snapshot
                

 Ví dụ, bộ cài đặt của SDK bên dưới đây dành cho môi trường phát triển 64-bit development, 
 kiến trúc đích là i586-tuned target architecture, và ảnh mà từ đó nó được build là `core-image-
sato` sử dụng phiên bản 2.2 snapshot của Yocto Project:

    
    
         poky-glibc-x86_64-core-image-sato-i586-toolchain-ext-2.2.sh
                

### Ghi chú 

 Nếu không muốn tải bộ cài đặt SDK, bạn hoàn toàn có thể tự build một bộ cài đặt SDK cho mình. 
 Thông tin về việc làm thế nào để build một một bộ cài đặt, bạn có thể xem chương "Building an SDK Installer"
. Hoặc một tài liệu khác nói về việc build bộ cài đặt, đó là trang wiki [Cookbook
guide to Making an Eclipse Debug Capable Image](https://wiki.yoctoproject.org/
wiki/TipsAndTricks/RunningEclipseAgainstBuiltImage). 
Trang wiki này tập trung vào quá trình phát triển sử dụng Eclipse IDE.

 Mặc định thì SDK, Toolchain và các file sau khi được cài đặt sẽ nằm ở thư mục
`poky_sdk` trong thư mục Home của bạn. Bạn có thể chọn bất cứ chỗ nào khác trong quá trình cài đặt
. Tuy nhiên, cần nhớ rằng thư mục bạn cho cho phép quyền ghi với những user sẽ sử dụng SDK, 
 Bởi vì nhiều file sẽ được ghi vào đó trong quá trình chạy SDK.

 Các hướng dẫn bên dưới đây sẽ chỉ ra cách chạy bộ cài đặt từ file nén chứa Toolchain
 môi trường phát triển với kiến trúc 64-bit x86 và build cho môi trường đích cũng là 64-bit x86 
 Giả định rằng bộ cài đặt của SDK nằm ở thư mục `~/Downloads/`.

### Ghi chú 

 Trong quá trình cài đặt, nếu bạn không có quyền ghi vào thư mục bạn chọn để cài
 bộ cài đặt sẽ báo cho bạn biết và exit. Hãy chắc chắn rằng bạn có quyền ghi đến thư mục
đã chọn một lần nữa.

    
    
         $ ./poky-glibc-x86_64-core-image-minimal-core2-64-toolchain-ext-2.2.sh
         Poky (Yocto Project Reference Distro) Extensible SDK installer version 2.2
         ===================================================================================
         Enter target directory for SDK (default: ~/poky_sdk):
         You are about to install the SDK to "/home/scottrif/poky_sdk". Proceed[Y/n]? Y
         Extracting SDK......................................................................done
         Setting it up...
         Extracting buildtools...
         Preparing build system...
         done
         SDK has been successfully set up and is ready to be used.
         Each time you wish to use the SDK in a new shell session, you need to source the environment setup script e.g.
          $ . /home/scottrif/poky_sdk/environment-setup-core2-64-poky-linux
                

## 2.3. Chạy script thiết lập môi trường cho SDK mở rông

 Sau khi đã có một SDK được cài đặt rồi, bạn phải chạy script thiết lập môi 
trường cho SDK trước khi thực sự sử dụng nó. Script này sẽ nằm ở thư mục bạn chọn lúc cài đặt,
 mặc định là `poky_sdk` nếu bạn không chọn thư mục khác.

 Trước khi chạy script hãy chắc chắn rằng tên script đúng với kiến trúc bạn đang phát triển.
 Tên script được bắt đầu bằng "`environment-setup`", sau đó là tên ngắn gọn của kiến trúc máy đích. 
 Ví dụ, các câu lệnh bên dưới đây sẽ chuyển thư mục hiện tại về thư mục cài đặt, rồi chạy (source) 
script thiết lập môi trường.
 Trong ví dụ này, script sẽ thiết lập một trường cho một máy dựa trên kiến trúc IA sử dụng i586 tunning:

    
    
         $ cd /home/scottrif/poky_sdk
         $ source environment-setup-core2-64-poky-linux
         SDK environment now set up; additionally you may now run devtool to perform development tasks.
         Run devtool --help for further details.
                

 Sau khi chạy script trên, sẽ có rất nhiều biến môi trường được định nghĩa:

    
    
         [SDKTARGETSYSROOT](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-SDKTARGETSYSROOT) - Đường dẫn đến sysroot được sử dụng trong cross-compilation
         [PKG_CONFIG_PATH](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-PKG_CONFIG_PATH) -  Được dẫn đến các file cấu hình package (pkg-config files)
         [CONFIG_SITE](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-CONFIG_SITE) - Nơi chứa các file preconfigure của GNU autoconf dành cho the target
         [CC](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-CC) - Chứa câu lệnh và các tham số tối thiểu của C compiler
         [CXX](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-CXX) - Chứa câu lệnh và các tham số tối thiểu của C++ compiler.
         [CPP](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-CPP) - Chứa câu lệnh và các tham số tối thiểu của C preprocessor
         [AS](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-AS) - Chứa câu lệnh và các tham số tối thiểu của assembler
         [LD](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-LD) - Chứa câu lệnh và các tham số tối thiểu của linker
         [GDB](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-GDB) - Chứa câu lệnh và các tham số tối thiểu của GNU Debugger
         [STRIP](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-STRIP) - Chứa câu lệnh và các tham số tối thiểu của 'strip', công cụ thực hiện rút gọi symbol (strip symbol) 
         [RANLIB](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-RANLIB) - Chứa câu lệnh và các tham số tối thiểu của 'ranlib'
         [OBJCOPY](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-OBJCOPY) - Chứa câu lệnh và các tham số tối thiểu của 'objcopy'
         [OBJDUMP](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-OBJDUMP) - Chứa câu lệnh và các tham số tối thiểu của 'objdump'
         [AR](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-AR) - Chứa câu lệnh và các tham số tối thiểu của 'ar'
         [NM](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-NM) - Chứa câu lệnh và các tham số tối thiểu của 'nm'
         [TARGET_PREFIX](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-TARGET_PREFIX) - Tiền tố của toolchain cho các công cụ phía target.
         [CROSS_COMPILE](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-CROSS_COMPILE) - Tiền tố của toolchain cho các công cụ phía target.
         [CONFIGURE_FLAGS](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-CONFIGURE_FLAGS) -  Tham số tối thiểu cho GNU configure
         [CFLAGS](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-CFLAGS) - C flags
         [CXXFLAGS](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-CXXFLAGS) - C++ flags
         [LDFLAGS](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-LDFLAGS) - linker flags khi sử dụng CC để link
         [CPPFLAGS](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-CPPFLAGS) -preprocessor flags
                

## 2.4. `devtool` trong luồng phát triển sử dụng SDK 

 Các đem lại sự khác biệt cho SDK chính là công cụ dòng lệnh tên là `devtool`.
 Công cụ này cung cấp một loạt tính năng giúp bạn build, test và đóng gói phần mềm, 
 và có thể tích hợp nó vào hệ thống build OpenEmbedded nữa.

 Công cụ dòng lệnh `devtool` được quản lý ở kho [Git](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#git), trong đó mỗi chức năng có một loạt sub-command. Bạn có thể chạy `devtool
--help` để xem toàn bộ commmand của nó.

 Có 3 sub-command của `devtool` để cung cấp cho các thao tác cơ bản cho quá trình phát triển:

  * _`devtool add`_: Hỗ trợ việc thêm một gói phần mềm vào để build. 

  * _`devtool modify`_: Thiết lập một môi trường cho phép bạn sửa source các thành phần có sẵn. 

  * _`devtool upgrade`_: Update các recipe có sẵn để bạn có thể build các file được cập nhật . 

 Do hệ thống build là OpenEmbedded, các "recipes" sẽ biểu diễn các gói phần mềm khi sử dụng `devtool`. 
 Khi sử dụng `devtool add`, một recipe sẽ tự động được tạo. Khi bạn sử dụng `devtool modify`, 
 recipe được chỉ định sẽ được dùng để xác định cần lấy source bằng cách nào và patch nó như thế nào. 
 Trong cả 2 trường hợp trên, một môi trương được thiết lập để cho phép thay đổi source theo ý muốn,
 khi định build một source tree của một recipe bất kì. Mặc định thì, các recipe và sources sẽ đều
nằm ở thư mục "workspace" nằm bên dưới SDK.

 Phần của lại sẽ miêu tả về các workflows khi sử dụng `devtool add`, `devtool modify`,
 và `devtool upgrade`.

### 2.4.1. Sử dụng `devtool add` để thêm ứng dụng

 Lệnh `devtool add` sẽ sinh một recipe mới dựa trên một source đã có sẵn. Command này tận dụng lợi thế của 
 lớp [workspace]http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html
#devtool-the-workspace-layer-structure) mà rất nhiều command `devtool` sử dụng. 
 Command này rất linh hoạt, nó cho phép vừa cho phép bạn giải nén source đến workspace 
 vừa cho phép đẩy vào kho local Git riêng để sử dụng mà không cần giải nén.
 
 Phụ thuộc vào tình huống cụ thể của bạn, các tham số và option truyền cho 
`devtool add` sẽ có nhiều dạng khác nhau. Hình sau sẽ biểu diễn một cách phổ biến của `devtool add` command:

![](figures/sdk-devtool-add-flow.png)

  1. _Sinh ra một recipe mới_: Phần đầu chỉ ra 3 tình huống sử dụng `devtool add` để sinh một recipe mới dựa trên source sẵn có.

 Trong môi trường phát triển chia sẻ, đây là một tình huống hết sức phổ biến, khi mỗi developer chịu 
trách nhiệm cho một phần code. Và trong trường hợp này, một developer mong muốn sử dụng source code
như là một phần của quá trình phát triển thông qua Yocto Project. Tất cả những gì bạn cần là có thể truy
cập vào source code, recipe và một khu vực được quản lý những cái bạn đang làm.

 Trên biểu đồ ở trên, có 3 tình huống sử dụng `devtool add`:

    * _Ngữ cảnh bên trái_: Ngữ cảnh của một tình huống phổ biến khi source không có ở local mà phải tải về giải nén nó. Trong tình huống này, bạn hãy cho phép nó được giải nén đến thư mục mặc định của workspace - bạn không muốn chỉ định một nơi nào khác ngoài workspace. Vì thế, mọi thứ bạn cần là đặt nó vào đâu trong workspace thôi :


         $ devtool add _recipe fetchuri_


 Với command này, `devtool` sẽ tạo một recipe vào thêm vào workspace, cũng như giải nến source vào một kho local Git trong thư mục `sources`.

    * _Ngữ cảnh ở giữa_: Ngữ cảnh này cũng mô tả tình huống khi source không có ở local, phải lấy về giải nén. Trong trường hợp này, source cũng được lấy về, giải nén vào đâu đó ở local - lần này nó nằm ngoài khu vực của workspace. Nếu yêu cầu, `devtool` sẽ luôn tạo một kho Git trong quá trình lấy source. Hơn nữa, tham số có vị trí đầu tiên _`srctree`_ trong trường hợp này sẽ chi cho `devtool add` biết source sẽ được giải nén vào đâu:


         $ devtool add _recipe srctree fetchuri_


 Tóm lại, source sẽ được lấy từ _`fetchuri`_ và được giải nén vào _`srctree`_ như là một kho Git tại local.

 Bên trong workspace, `devtool` sẽ tạo cả recipe lẫn append file cho source này.

    * _Ngữ cảnh bên phải_: Ngữ cảnh của tình huống mà source code (srctree) nằm được chuẩn bị bên ngoài thư mục `devtool` workspace. 

 Câu lệnh sau yêu cầu một tên của recipe và nơi chúng được chứa:

    
    
         $ devtool add _recipe srctree_
                                    

 Câu lệnh trên sẽ đánh giá source rồi tạo recipe cho nó trong thư mục của workspace.

 Vì source code đã tồn tại rồi nên `devtool` sẽ không cố gắng mang nó vào worksapce nữa 
- chỉ có recipe tương ứng với nó mới được đặt vào workspace thôi.

 Cũng trong thư mục của recipe, câu lệnh trên cũng tạo một thư mục append và 
 thêm các file `*.bbappend` vào trong đó.

  2. _Chỉnh sửa recipe_: Tới thời điểm này, bạn có thể sử dụng `devtool edit-recipe` để mở một editor, cái được set bằng biến môi trường `$EDITOR`, sau đó chỉnh sửa recipe đã chỉ định: 
    
    
         $ devtool edit-recipe _recipe_
                            

Trong editor, bạn có thể tạo ra bất cứ thay đổi nào cho recipe, và những thay đổi đó sẽ được nhận biết 
nếu build lại.

  3. _Build một recipe hoặc rebuild cả Image_: Đến thời điểm này rồi, các bước tiếp theo bạn sẽ làm phụ thuộc bạn định làm gì với source mới.

 Nếu bạn cần kết quả build hay thậm chí đưa đưa xuống phần cứng đích, bạn có thể sử dụng `devtool build`:

    
    
         $ devtool build _recipe_
                            

 Mặt khác, bạn muốn một ảnh hệ thống chứa các gói từ recipe để triển khai ngay lập tức lên thiết bị 
 ( ví dụ: cho mục đích testing chẳng hạn), bạn có thể sử dụng câu lệnh `devtool build-image`:

    
    
         $ devtool build-image _image_
                            

  4. _Triển khai kết quả build_: Khi bạn sử dụng `devtool build` để build recipe của bạn, thì hầu như sẽ muốn kiểm trả xem kết quả có như mong đợi trên thiết bị thật hay không. 

### Ghi chú 

 Bước này giả định rằng bạn đã một ảnh hệ thống được chạy trên  
QEMU hoặc trên phần cứng thật. Và cũng giả định rằng ảnh hệ thống chạy trên phần cứng thật có hỗ trợ SSH
cho phép bạn triển khai mọi thứ qua đường truyền mạng.
 Bạn có thể triển khai trên phần cứng thật sử dụng command sau `devtool deploy-target`:

    
    
         $ devtool deploy-target _recipe target_
                            

_`target`_ là môi trường đích, nơi bạn chạy SSH server.

 Tất nhiên, bạn cũng có thể triển khai một ảnh hệ thống bằng câu lệnh build lại ảnh `devtool build-
image`. Tuy nhiên, `devtool` không cung cấp một command cụ thể nào để bạn triển khai.

  5. _Kết thúc việc với recipe_: Câu lệnh `devtool finish` sẽ tạo patch rồi commit đến kho Git, di chuyển recipe sang hẳn một layer vĩnh viễn, sau đó thì recipe sẽ được reset trạng thái chứ không phải nằm ở workspace nữa. 
    
    
         $ devtool finish _recipe layer_
                            

### Note

 Mọi thay đổi bạn muốn đưa vào patch thì phải được commit đến kho git của source tree.

 Như đã nói ở trên, `devtool finish` sẽ di chuyển recipe đến layer của nó vĩnh viễn.

 Quá trình cuối cùng của `devtool finish`, trạng thái của layer chuẩn và upstream sẽ được phục hồi
vì thế bạn cũng có thể tiếp tục build source từ đầu.

### Ghi chú 

 Bạn có thể sử dụng câu lệnh`devtool reset` để quay về trạng thái như chưa làm gì nếu bạn không muốn tiếp tục
công việc nữa. Khi thực hiện câu lệnh này, hãy nhớ rằng source tree vẫn còn nguyên đấy.

### 2.4.2. Sử dụng `devtool modify` để sửa một thành phần đã có sẵn 

`devtool modify` được đưa ra cho tình huống khi làm việc với source 
mà recipe đi kèm. Command này đủ linh hoạt để bạn giải nén code,  
 chỉ định recipe, quản lý các bản patch từ các developer khác có liên quan đến source của bạn.

 Phụ thuộc vào ngữ cảnh cụ thể, tham số và options khi sử dụng với 
`devtool modify` cũng có nhiều dạng khác nhau. Hình bên dưới đây sẽ chỉ ra một
trường hợp sử dụng phổ biến của `devtool modify`:

![](figures/sdk-devtool-modify-flow.png)

  1. _Chuẩn bị để chuẩn bị source code_: Phần trên chỉ ra 3 ngữ cảnh bạn có thể sử dụng `devtool modify` để chuẩn bị làm việc với source code. Mỗi ngữ cảnh sẽ giả định như sau: 

    * Recipe nằm ở layer bên ngoài workspace của `devtool`. 

    * Source có có trên upstream ở trạng thái chưa được giải nén hoặc đã được giải nén ở local những phiên bản cũ. 

 Tình huống phổ biến cho trường hợp này là khi một developer khác tạo layer sử dụng với Yocto Project và recipe của họ nằm trong layer đó rồi.
 Hơn nữa, source lại nằm ở upstream hoặc local thôi.

    * _Bên trái_: Ngữ cảnh bên trái miêu tả một tình huống phổ biến, khi source không có ở local và cần được tải về giả nén. Trong tình huống này, mặc định source sẽ được giải nén vào thư mục của workspace. Các recipe sẽ nằm trong layer, cái mà nằm bên ngoài workspace ( Ví dụ `meta-`_`layername`_). 

 Câu lệnh sau được chỉ định recipe và mặc định sẽ giải nén các file source code:

    
    
         $ devtool modify _recipe_
                                    

 Một khi `devtool` xác định được vị trí của biến
[`SRC_URI`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html
#var-SRC_URI), nó sẽ biết được vị trí của source code và vị trí các file patch đến từ các developer khác. 

### Ghi chú 

 Bạn không thể sử dụng một URL cho source code  _`srctree`_ khi sử dụng câu lệnh `devtool modify`.

 Với ngữ cảnh này thì không hề có tham số _`srctree`_ , 
`devtool modify` sẽ giải nén source code vào một cấu trúc sử dụng Git. 
 Hơn nữa, vị trí mặc định sẽ ở bên dưới workspace. Kết quả của câu lệnh này là source code và các file append
sẽ được thêm vào project trong khi recipe của nó vẫn ở vị trí cũ.

    * _Ở giữa_: Ngữ cảnh cho tình huống khi source code không có ở local. Trong trường hợp này, một lần nữa source nằm ở upstream, nó cần được lấy về lưu vào một kho Git. Một lần nữa, recipe và layer của nó lại nằm bên ngoài workspace.

 Câu lệnh sau đây sẽ nói cho `devtool` biết recipe nào bạn muốn làm việc, trong trường hợp này
, trong trường hợp này là chỉ ra các các file source code nằm ngoài workspace.
    
    
         $ devtool modify _recipe srctree_
                                    

 Đối với tất cả các thao tác giải nén, command sẽ sử dụng `SRC_URI` của recipe để xác định các file source code 
 Khi xác định được vị trí rồi, nó sẽ thực hiện việc giải nén. Cung cấp tham số _`srctree`_ để cho `devtool` source sẽ được giải nén ra.

 Bên trong workspace, `devtool` sẽ tạo các file append cho recipe. Các recipe sẽ vẫn ở nguyên vị trí của nó
nhưng source được giải nén vào _`srctree`_.

    * _Bên phải_: Ngữ cảnh bên phải miêu tả tình huống mà source code(_`srctree`_) đã tồn tại trước đó trong một
cấu trúc của kho Git nằm ngoài workspace của `devtool` workspace. Trong ví dụ này, recipe cũng ở đâu đó trong layer của nó. 

 Câu lệnh sau sẽ nói cho `devtool` biết cái recipe nào bạn muốn làm việc, 
 sử dụng  tham số "-n" để báo rằng không cần phải giải nén source code nữa, sử dụng 
_`srctree`_ để chỉ ra nơi của source trước đó:

    
    
         $ devtool modify -n _recipe srctree_
                                    
 
 Khi câu lệnh trên kết thúc, nó chỉ tạo 1 file append cho recipe bên trong workspace mà thôi. 
 Cái recipe và source chính của nó vẫn ở vị trí cũ.

  2. _Sửa source code_: Một khi bạn đã sử dụng câu lệnh `devtool modify`, bạn có thể thoải mái sửa source bằng bất cứ editor nào bạn muốn và save lại thôi. 

  3. _Build Recipe_: Sau khi đã update các source file, bạn có thể tiến hành build lại recipe . 

  4. _Triển khai kết quả build_: Khi sử dụng câu lệnh `devtool build` để build recipe của bạn, bạn thường muốn xem kết quả có như mong đợi trên phần cứng đích. 

### Ghi chú 

 Bước tiếp theo giả định rằng bạn đã có sẵn một ảnh hệ thống có thể chạy trên
QEMU hoặc phần cứng thật rồi. Dành cho việc triển khai trên phần cứng thật, thì cũng
giả định rằng bạn có một hệ thống đã có sẵn SSH có thể truy cập qua kết nối mạng.

 Bạn có thể triển khai kết quả build dựa trên phần cứng thật bằng câu lệnh sau `devtool deploy-target`:

    
    
         $ devtool deploy-target _recipe target_
                            

_`target`_ là một máy target đang chạy SSH server.

 Tất nhiên bạn có thể tạo ra một ảnh hệ thống bằng câu lệnh `devtool build-
image`. Tuy nhiên, devtool không cung cấp câu lệnh để bạn làm điều này.

  5. _Kết thúc công việc vớiRecipe_: Câu lệnh `devtool finish` sẽ tạo bất cứ bản nào cho bất kì commit nào được gửi đến Git repository cho phép update các recipe sử dụng ( hoặc tạo các file `.bbappend` để làm điều tương tự, dựa trên trạng thái của layer đích), cuối cùng reset trạng thái cho recipe để nó có thể được build một cách bình thường chứ không bắt buộc phải từ workspace nữa. 
    
    
         $ devtool finish _recipe layer_
                            

### Ghi chú 

 Bất cứ thay đổi nào bạn muốn chuyển thành patch phải được commit lên kho Git.

 Vì không cần phải thay đổi chỗ của recipe, nên câu lệnh `devtool finish` hoặc sẽ update
recipe ở vị trí ban đầu hoặc sẽ tạo một file `.bbappend` trong một layer mà được set bởi _`layer`_.

 Kết thúc câu lệnh `devtool finish` trạng thái của layer ban đầu và workspace được
phục hồi vì thế bạn có thể build từ chỗ khác chứ không chỉ từ workspace.

### Ghi chú 

 Bạn có thể sử dụng câu lệnh `devtool reset` để đưa trạng thái recipe về ban đầu bất cứ khi nào
bạn không muốn tiếp tục làm việc với recipe nữa. Khi thực hiện câu lệnh này, bạn sẽ thấy rằng source
tree vẫn được giữ lại.

### 2.4.3. Sử dụng câu lệnh `devtool upgrade` để tạo một phiên bản của Recipe
support phiên bản mới hơn của phần mềm

 Sử dụng câu lệnh `devtool upgrade` để update một recipe có sẵn giúp bạn
có thể build một tập các source file mới. Command này đủ linh hoạt để cho phép bạn
chỉ ra cấu trúc revision và versioning, cũng như giải nén source ra ngoài/hoặc vào bên trong 
 workspace của `devtool`, giúp bạn làm việc với bất cứ source code nào Yocto đang hỗ trợ.

 Phụ thuộc vào ngữ cảnh cụ thể của bạn mà tham số và option cho 
`devtool upgrade` sẽ có nhiều dạng khác nhau. Hình bên dưới đây ra chỉ ra một 
trường hợp phổ biến của câu lệnh `devtool modify`:

![](figures/sdk-devtool-upgrade-flow.png)

  1. _Chuẩn bị upgrade_: Phần trên chỉ ra một tình huống thông thường sử dụng `devtool upgrade`. Một số điều kiện giả định: 

    * Một số recipe nằm ở các layer bên ngoài workspace của `devtool`. 

    * Các file source của phiên bản mới thường nằm cùng hoặc vị trí tương tự với địa chỉ ở [`SRC_URI`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-SRC_URI) được quy định trong recipe ( ví dụ: một file nén tarball với số phiên bản mới trong tên, revision từ Git repository của upstream). 

 Một tình huống phổ biến là các phần mềm bên thứ 3 (third-party) thường có một revision
mà nó được update. Cái recipe cũng được access tương tự cái layer của bạn. 
 Vì thế, bạn cần upgrade recipe để sử dụng phiên bản mới của phần mềm:

    
    
         $ devtool upgrade -V _version recipe_
                            

 Mặc định, câu lệnh `devtool upgrade` sẽ giải nén source xuống thư mục
`sources` bên dưới workspace. Nếu bạn muốn giải nến đến bất cứ chỗ nào khác 
 bạn cần cung cấp giá trị _`srctree`_ ở tham số như câu lệnh bên dưới đây:

    
    
         $ devtool upgrade -V _version recipe srctree_
                            

 Cũng trong ví dụ này, ta thấy tham số "-V" được sử dụng để chỉ định một phiên bản mới.
 Nếu source được chỉ định bởi `SRC_URI` trong recipe là một kho Git, thì bạn phải chỉ định 
 thêm tham số "-S" để chỉ rõ revision của phần mềm.

 Một khi `devtool` xác định được vị trí các recipe, nó sẽ sử dụng biến `SRC_URI` để xác định source code
cũng như các bản patch từ các developer khác.
 Cuối cùng, command sẽ setup source code, một phiên bản mới của recipe, 
 và thêm file vào workspace.

  2. _Giải quyết các tranh cấp khi thực hiện Upgrade_: Ở thời điểm này, có thể xảy ra một vài "tranh chấp" (2 phiên bản phần mềm cùng sửa 1 chỗ) khi thực hiện upgrade phiên bản. Điều này xảy ra khi một số patch file bạn chỉ định trong `SRC_URI` có các thay đổi không khớp với phiên bản mới. Nếu xảy ra trường hợp này, chẳng còn cách nào khác bạn buộc phải edit lại source để xem các vị trí bị tranh chấp đó cùng với câu lệnh giải quyết tranh cấp `git rebase`.

 Trước khi sang bước tiếp theo, bạn hãy chắc chắn rằng các tranh chấp đã được giải quyết hết.

  3. _Build lại recipe_: Một khi đã có một dãy các recipe rồi, bạn có thể build nó. Bạn có thể sư dụng câu lệnh `devtool build` hoặc `bitbake`. Kết quả build sẽ được lưu trong thư mục [`TMPDIR`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-TMPDIR). 

  4. _Triển khai kết quả build_: Khi bạn sử dụng câu lệnh `devtool build` hoặc `bitbake` để build recipe của bạn,  bạn thường muốn xem những thay đổi có được như mong muốn trên phần cứng đích. 

### Ghi chú 

 Bước này giả định rằng bạn đã từng build ảnh hệ thống cho QEMU hoặc phần cứng thật trước đó rồi.
  Và cũng giả định luôn rằng có một SSH server chạy trên ảnh hệ thống đó. Rồi nếu bạn chạy trên phần
cứng thật thì giả định có thể truy cập bằng đường mạng đến máy đích từ máy phát triển.

 Bạn có thể deploy kết quả build xuống phần cứng thật sử dụng câu lệnh `devtool deploy-target`:

    
    
         $ devtool deploy-target _recipe target_
                            

 _`target`_  chỉ máy đích, có SSH server đang chạy trên đó.

 Tất nhiên bạn vẫn có thể sử dụng câu lệnh `devtool build-
image` để triển khai xuống phần cứng thật. Tuy nhiên, `devtool` không cung cấp cụ thể sau đó.

  5. _Kết thúc phiên làm việc với Recipe_: Câu lệnh `devtool finish` có thể tạo bản patch cho bất cứ commit nào đến kho Git Local, sử dụng khi di chuyển recipe đến một layer khác, hoặc reset lại recipe để nó có thể được build bình thường như các recipe khác. Nếu layer đích chính là layer nguồn, recipe và các file liên quan của phiên bản cũ sẽ được thay thế bởi phiên bản mới. 
    
    
         $ devtool finish _recipe layer_
                            

### Ghi chú 

 Mọi thay đổi muốn trở thành các bản patch đều phải được commit đến kho Git Local.

 Câu lệnh kết thúc quá trình làm việc `devtool finish`, trạng thái chuẩn của các layer và 
các source stream sẽ được trở về trạng thái chuẩn, vì thế bạn có thể build như bình thường thành vì
từ những thứ trong workspace.

### Ghi chú 

 Bạn cũng có thể sử dụng câu lệnh `devtool reset` để đưa mọi thứ trở về trạng thái ban đầu
nếu không muốn tiếp tục các xử lý với recipe nữa. Nếu bạn sử dụng câu lệnh này, thì hãy nhớ
các source đã tải vẫn còn nguyên nha, dù nó không ảnh hưởng gì.

## 2.5. Một cái nhìn gần vào `devtool add`¶

 Câu lệnh `devtool add` tự động tạo một recipe dựa trên cấu trúc source bạn cung cấp
cho nó. Hiện tại, câu lệnh này hỗ trợ những dạng dưới đây:

  * Autotools (`autoconf` and `automake`) 

  * CMake 

  * Scons 

  * `qmake`

  * Plain `Makefile`

  * Out-of-tree kernel module 

  * Binary package (i.e. "-b" option) 

  * Node.js module 

  * Python modules that use `setuptools` or `distutils`

Apart from binary packages, việc phát hiện source được tổ chức như thế nào
nên được thực hiện một cách tự động dựa trên trạng thái các file hiện tại. 
 Ví dụ, nếu có `CMakeLists.txt`, thì sẽ coi như chúng sử dụng CMake và sẽ
build, chạy theo cách của CMake.

### Ghi chú 

 Trong hầu hết trường hợp, bạn cần edit lại các recipe được sinh tự động để
có thể build được chúng. Thông thường, bạn sẽ phải xem qua một vài file rồi
edit chúng đến khi việc build không còn lỗi nữa. Khi recipe được build rồi, bạn
có thể tiếp tục với các thao tác khác để test chúng trên thiết bị đích.

 Phần còn lại của chương sẽ chỉ ra làm thế nào các thành phần của recipe được
sinh ra.

### 2.5.1. Tên và phiên bản 

 Nếu bạn không chỉ định tường minh tên và phiên bản trên dòng lệnh, câu lệnh `devtool add`
 sẽ cố gắng phát hiện tên và phiên bản từ các meta data trong chính source code. 
 Sau đó nó sẽ set tên của recipe tương ứng. Nếu nó không thể phát hiện ra tên và phiên bản, 
 câu lệnh `devtool add` sẽ hiển thị lỗi và bạn phải chạy lại với tên và phiên bản được set.

 Thỉnh thoảng tên và phiên bản phát hiện được cũng không đúng
. Với những trường hợp như thế, bạn phải reset lại recipe:

    
    
         $ devtool reset -n _recipename_
                    

 Sau khi chạy câu lệnh `devtool reset` command, bạn cần chạy lại `devtool add` một lần nữa
với tên và phiên bản được chỉ định trên dòng lệnh.

### 2.5.2. Phát hiện phụ thuộc và mapping 

 Câu lệnh `devtool add` có gắng phát hiện các phụ thuộc của recipe hiện tại
và map chúng với các recipe đang có sẵn. Trong quá trình mapping, nó sẽ thêm tên của các recipe
đó vào biên môi trường trong recipe hiện tại [`DEPENDS`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-DEPENDS). Nếu có phụ thuộc nào không thể map được thì sẽ co một comment
được đưa vào để chỉ ra điều đó. Việc không map được có thể do tên không khớp,
hoặc đơn giản là không có recipe nào cung cấp phụ thuộc đó. Trong trường hợp đó, bạn phải sử dụng
 câu lệnh `devtool add` để thêm các recipe chứa các phụ thuộc trước, rồi quay lại recipe ban đầu để thêm các recipe tương ứng vào biến `DEPENDS` như ở trên.

 Nếu bạn có những phụ thuộc dạng run-time, bạn có thể thêm chúng theo cách sau:

    
    
         RDEPENDS_${PN} += "dependency1 dependency2 ..."
                    

### Ghi chú 

 Câu lệnh `devtool add` thường không thể phân biệt được cái nào là phụ thuộc bắt buộc, cái nào là không bắt buộc.
 Dẫn đến, một số phụ thuộc được phát hiện hóa ra lại là không bắt buộc. 
 Khi còn nghi ngờ điều đó, bạn cần xem kĩ lại tài liệu của phần mềm muốn đưa vào recipe đó
để xem chính xác đó là những gì. Trong một vài trường hợp, nếu có thể tìm thấy một vài tham số truyền cho configure script để bỏ bớt một vài chứng năng không cần thiết, dẫn đến sẽ bớt đi được phụ thuộc.

### 2.5.3. Phát hiện license 

 Câu lệnh `devtool add` sẽ cố gắng phát hiện xem phần mềm đang được thêm vào
được phân phối dưới giấy phép mã nguồn mở phổ biến nào, và gán giá trị
[`LICENSE`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html
#var-LICENSE) tương ứng. Bạn nên kiểm tra thật kĩ, cả tài liệu lẫn source code
của phần mềm đang muốn build để xác định chính xác license.

 Câu lệnh `devtool add` cũng gán giá trị [`LIC_FILES_CHKSUM`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-
manual.html#var-LIC_FILES_CHKSUM) cho tất cả các file có liên quan đến vấn đề license. 
 Tuy nhiên, các tuyên bố về license thường xuất hiện ở ngay đầu source hoặc tài liệu.
  Do đó, bạn cần điều chỉnh giá trị biến `LIC_FILES_CHKSUM` trỏ đến một hoặc nhiều file như thế. 
 Việc thiết lập giá trị biến `LIC_FILES_CHKSUM` đặc biệt quan trọng khi sử dụng phần mềm từ bên thứ 3
(third-part software). Cơ chế về license đảm bảo cho bạn sử dụng đúng license khi update
trong tương lai nữa. Bất cứ thay đổi nào liên quan đến license đều được phát hiện và thông báo
đến bạn, do đó, bạn cần check lại những chỗ đó.

 Nếu câu lệnh `devtool add` không thể phát hiện thông tin về license, giá trị biến 
`LICENSE` được gán là "CLOSED", và giá trị `LIC_FILES_CHKSUM` sẽ không được gán gì hết. 
 Điều này giúp bạn tiếp tục quá trình phát triển của mình, nhưng không phải bao giờ cũng là phù hợp. 
 Bởi vậy, bạn nên kiểm tra tài liệu hoặc source để biết được license thực sự là gì.

### 2.5.4. Thêm phần mềm chỉ có Makefile

 Chính `make` cũng là một cách rất phổ được sử dụng trong cả phần mềm mã nguồn mở lẫn nguồn đóng. 
 Thật không may, hầu hết Makefile không được viết để có thể cross-platform. 
 Vì thế, câu lệnh `devtool add` thường không làm được gì nhiều để đảm bảo các Makefile này 
được build chính xác. Một ví dụ rất phổ biến là chỉ định `gcc` thay vì sử dụng giá trị biến 
[`CC`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-CC)
. Thông thường, trong môi trường cross-compilation, `gcc` thường nó đến compiler của host,
còn cross-compiler thường có tên kiểu như `arm-poky-linux-gnueabi-gcc` và một vài tham số khác 
( ví dụ: chỉ định đường dẫn của sysroot của máy đích chẳng hạn).

Khi viết một recipe cho phần mềm chỉ có Makefile, hãy nhớ rằng:

  * Bạn có thể cần sửa lại Makefile để sử dụng các giá trị biến chứ không phải chỉ định hardcoding như `gcc` và `g++`. 

  *  Môi trường để chạy `make` thường được setup với một vài giá trị chuẩn cho việc compilation ( Ví dụ: `CC`, `CXX`, hoặc tương tự) tương tự với cách thiết lập được sử dụng trong script setup môi trường cho SDK. Các dễ nhất để thấy các giá trị này là sử dụng câu lệnh `devtool build` trên chính recipe đó, sau đó xem nội dung file `oe-logs/run.do_compile`. Ở ngay đầu file, bạn sẽ thấy danh sách các biến môi trường, cái sẽ được set. Bạn có thể tạo ra Makefile tương thích với các biến đó. 

  * Nếu Makefile gán giá trị mặc định cho biến sử dụng "=", thì các giá trị mặc định đó sẽ ghi đè nên các giá trị sẵn có của môi trường, và đó là điều không mong đợi. Trong tình huống này, bạn cần sửa lại Makefile để nó sử dụng toán tử "?=", hoặc gán thông qua các tham số từ dòng lệnh `make`. Để truyền giá trị cho kiểu như thế, bạn có thể thêm giá trị biến [`EXTRA_OEMAKE`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-EXTRA_OEMAKE) or [`PACKAGECONFIG_CONFARGS`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-PACKAGECONFIG_CONFARGS) bên trong recipe. Dưới đây là ví dụ sử dụng `EXTRA_OEMAKE`: 
    
    
         EXTRA_OEMAKE += "'CC=${CC}' 'CXX=${CXX}'"
                            

 Ở ví dụ ở trên, dấu nháy đơn được sử dụng bọc biểu thực giá trị biến môi trường
khi giá trị có thể chứa dấu cách vì đây là các option mặc định cho compiler.

  * Việc để hardcode đường dẫn trong Makefiles thường gây ra vấn đề khi sử dụng môi trường cross-compilation. Điều này đúng là vì các đường dẫn đó thường chỉ một nơi trên môi trường build, thường sẽ không phù hợp với cross-compilation. Cần phải sửa lại Makefile cho phù hợp. 

  * Thỉnh thoảng Makefile chứa câu lệnh chỉ dành cho target như `ldconfig`. Với những trường hợp như này bạn có đơn giản là comment bỏ dòng đó đi. 

### 2.5.5. Thêm một tool native 

 Thông thường, thông thường bạn sẽ cần nhiều tool thêm trên môi trường build để tương ứng với target.
 Về việc này, bạn nên chú ý những điểm sau khi làm việc với `devtool add`:

  * Chỉ định tên của các recipe có phần đuôi là "-native". Chính là tên các recipe cho công cụ tương ứng nhưng được build cho môi trường build. 

  * Chỉ định các recipe có tên chứa phần đuôi "also-native" khi sử dụng câu lệnh `devtool add`. Chỉ định này có nghĩa rằng, recipe được build cho target những cũng build cho cả môi trường build nữa, trong khi "-native" chỉ build cho host. 

### Ghi chú 

 Nếu bạn chỉ cần thêm một công cụ riêng lẻ, cái mà sẽ build code cho target, bạn có thể chỉ định riêng các recipe
dành cho việc build native và target thay vì để chung trong quá trình build 
 Và cũng để ý rằng với việc sử dụng "also-native", bạn có thể thêm công cụ mà chỉ cần sử dụng 1 recipe.

### 2.5.6. Thêm module Node.js 

 Bạn cũng có thể sử dụng câu lệnh `devtool add` để thêm một module Node.js theo 2 cách dưới đây:
: 1) Thông qua `npm` and, 2) Từ repo hoặc từ source tại local.

 Sử dụng câu lệnh như bên dưới đây để thêm module Node.js thông qua `npm`:

    
    
         $ devtool add "npm://registry.npmjs.org;name=forever;version=0.15.1"
                    

 Tham số tên và phiên bản là bắt buộc. Các file Lockdown và shrinkwrap được sinh ra
và được chỉ định bởi chính các recipe để gắn chúng với phiên bản của các file đã tải
trong lần đầu tiên. Nó cũng lưu lại checksum để xác thực khi có tải tiếp trong tương lại.
 Và tất cả những hành động này để đảm bảo tính tái hiện lại được và tính nhất quan của bạn build.

### Ghi chú 

  * Bạn phải sử dụng dấu nháy kép ở URL. Bản thân câu lệnh `devtool add` không yêu cầu dấu nháy, nhưng bản thân shell thì lại coi ";" là dấu ngăn cách giữa nhiều câu lệnh. Vì thế, nếu không có dấu nháy, câu lẹnh `devtool add` sẽ không nhận đủ tham số số, đồng thời cũng xuất hiệt một vài dòng kiểu "command not found". 

  * Để thêm được các Node.js modules, cần có recipe tên là `nodejs` trong SDK  của bạn để cung cấp chính Node.js. 

 Như đã nói ở phía trên, bạn cũng có thể thêm trực tiếp Node.js modules từ một repo hoặc từ chính
local. Để thêm theo cách đó, sử dụng câu lệnh `devtool add` theo cách như dưới đây:

    
    
         $ devtool add https://github.com/diversario/node-ssdp
                    

 Trong ví dụ này, câu lệnh `devtool` tải Git repository được chỉ định, phát hiện đó là Node.js code, 
 tự động lấy về bằng `npm`, và set [`SRC_URI`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html
#var-SRC_URI) tương ứng.

## 2.6. Làm việc với recipe 

 Khi build một recipe sử dụng `devtool build`, thông thường hệ thống build
sẽ thực hiện các bước sau:

  1. Lấy source code 

  2. Giải nén source code 

  3. Cấu hình source code 

  4. Biên dịch source code 

  5. Cài đặt các kết quả biên dịch 

  6. Đóng gói các kết quả biên dịch 

 Với các recipe đã nằm trong workspace, fetching và unpacking sẽ bị vô hiệu
nếu recipe đó đã được chuẩn bị, việc này để đảm bảo tính nhất quán. Mỗi bước trong quá trình
build được định nghĩa là một hàm , thường bắt đầu bởi tiền tố "do_". Những hàm này
có thể là các shell script hoặc cũng có thể viết bằng python.

 Nếu bạn từng xem nội dung của một recipe, bạn sẽ thấy rằng nó không chứa toàn bộ
các bước nhỏ để build phần mềm đó. Thay vào đó, các bước thông dụng được nhóm thành class và
được kế thường bằng từ khóa `inherit`, sau khi kế thừa thì recipe chỉ cần miêu tả những các dành riêng cho
phần mềm nó định build cho thôi. Một lớp [`base`](http://www.yoctoproject.org/docs/2.2/ref-
manual/ref-manual.html#ref-classes-base) được ngầm định kế thừa bởi tất cả các recipes để cung cấp
các chức năng mà hầu hết các recipe đều cần.

 Phần còn lại của chương này sẽ nói về các thông tin hữu ích khi làm việc với recipe.

### 2.6.1. Tìm các log và working file 

 Khi bạn debug các recipe mà bạn đã tạo lúc trước bằng câu lệnh `devtool add` lúc trước 
 hoặc source code bạn đang sửa sử dụng câu lệnh `devtool modify`,
 Kết quả từ câu lệnh build `devtool build`, bạn sẽ thấy có một vài symbol link được tạo 
bên trong thư mục : `oe-logs`, nó sẽ trỏ đến thư mục chứa log files cùng các run scripts 
 cho mỗi bước của quá trình build và `oe-workdir`, cái trỏ đến khu vực work tạm thời của mỗi recipe. 
 Bạn có thể sử dụng những thông tin này để biết chuyện gì đã xảy ra trong lúc build.

 Cụ thể nội dung từ thư mục dưới `oe-workdir` được cho là có ích:

  * `image/`: Chứa toàn bộ các file đã được cài đặt ở bước [`do_install`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#ref-tasks-install). Ở bên trong source code của recipe, thư mục này được tham chiếu bởi biểu thức `${`[`D`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-D)`}`. 

  * `sysroot-destdir/`: Chứ một tập con của các file được cài đặt ở bước `do_install` mà sẽ được đưa vào shared sysroot. Thông tin thêm về loại này, hãy xem chương "Sharing Files Between Recipes". 

  * `packages-split/`: Mỗi thư mục con trong này tương ứng với cái mà được recipe tạo ra. Thông tin thêm về loại này, xem chương "Packaging".

### 2.6.2. Thiết lập các tham số cấu hình 

 Nếu recipe cho sofware của bạn sử dụng GNU autoconf, một tập cố định các tham số
được pass để cho phép cross-compilation công với các tham số thêm được chỉ định bởi [`EXTRA_OECONF`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-EXTRA_OECONF) hoặc từ 
[`PACKAGECONFIG_CONFARGS`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-PACKAGECONFIG_CONFARGS) trong chính recipe đó. Vì thế, nếu bạn muốn thêm tham số cho quá trình configure, hãy thêm vào `EXTRA_OECONF` hoặc `PACKAGECONFIG_CONFARGS`. Nhưng hệ thống build khác cũng có cách tương tự,
( ví dụ: biến [`EXTRA_OECMAKE`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-EXTRA_OECMAKE) là dành cho CMake,
[`EXTRA_OESCONS`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-EXTRA_OESCONS) là dành cho Scons, cứ như vậy). Nếu bạn cần chuyển bất cứ thông tin nào cho câu lệnh `make` , bạn có thể sử dụng `EXTRA_OEMAKE` hoặc biến [`PACKAGECONFIG_CONFARGS`](http://www.yoctoproject.org/docs/2.2/ref-manual
/ref-manual.html#var-PACKAGECONFIG_CONFARGS). 

 Bạn có thể sử dụng câu lệnh `devtool configure-help` để xem thêm các biến đã nhắc tới ở đoạn trên. 
 Câu lệnh này sẽ đưa ra chính xác các option có thể được sử dụng, và cả cách kết sử dụng với `EXTRA_OECONF` or `PACKAGECONFIG_CONFARGS` nữa. Nếu có thể, câu lệnh cũng chỉ bạn đầu ra của lệnh configure với tham số help nữa.

### 2.6.3. Chia sẻ file giữa các recipe 

 Nhiều recipes sử dụng các file được cung cấp bởi các recipes khác trên máy build.
 Ví dụ, một ứng dụng được linking với một thư viện dùng chung cần biết cách để truy cập đến 
 chính các thư viện đó cũng như các file header liên quan. Điều này được giải quyết trong
SDK mở rộng (extensible SDK) thông qua sysroot. Mỗi sysroot đặc trưng cho 1
"machine" mà từ đó SDK được build. Trong thực tế, có một sysroot trên máy đich (target machine),
 và một sysroot trên máy build.

 Các recipe không bao giờ trực tiếp ghi file vào sysroot. Thay vào đó, các file được đưa vào một đường dẫn chung
 (standard locations) trong quá trình thực hiện task 
[`do_install`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#ref-tasks-install) được gọi là thư mục `${`[`D`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-
manual.html#var-D)`}`. Một tập nhỏ của các file đó sẽ tự động được đưa vào sysroot. 
 Lý do cho giới hạn này là tất cả các file được đưa vào sysroot phải được phân loại theo một danh mục đã được quy định trước để đảm bảo chúng có thể được xóa bỏ khi gỡ recipe ra khỏi ảnh hệ thống. Sau đó, sysroot mới lấy lại được không gian từ các file không còn được sử dụng nữa (stale files).

### 2.6.4. Đóng gói 

 Việc đóng gói không phải luôn luôn tối ưu trong SDK mở rộng.
Tuy nhiên, nếu bạn muốn đánh giá kết quả build được đưa vào ảnh hệ thống đích như thế nào, 
 thì chắc chắn phải hiểu về đóng gói (packaging) bởi vì nội dung của ảnh hệ thống được miêu tả bằng
khái niệm của package chứ không phải bằng các recip.

 Trong quá trình thực hiện task [`do_package`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-
manual.html#ref-tasks-package), các file được cài đặt khi chạy task 
[`do_install`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#ref-tasks-install) sẽ được đưa vào 1 package chính, thường là có cùng tên với recipe, 
 và một vài package khác. Lý do có sự phân chia này là vì không phải tất cả các file được 
cài đặt đó đều cần thiết cho mọi ảnh hệ thống. Ví dụ , bạn hầu như không cần bất cứ tài liệu nào trên ảnh hệ thống của sản phầm. Vì vậy, phần tài liệu trong mỗi recipe được đưa vào package có phần đuôi và `-doc`. 
 Rồi thì, các phần mềm có các module hoặc plugin cũng có thể thực hiện việc phân chia tương tự.

 Sau khi build một recipe, bạn có thể thấy các file đã được đi vào đâu bằng cách xem nội dung thư mục
`oe-workdir/packages-split`, nơi chứa một thư mục con cho mỗi package. Cho một vài trường hợp nâng cao, 
biến [`PACKAGES`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html
#var-PACKAGES) và biến [`FILES`](http://www.yoctoproject.org/docs/2.2/ref-manual
/ref-manual.html#var-FILES) được sử dụng để điều khiển việc chia gói. Biến môi trương `PACKAGES`
 liệt kê tất cả các package được tạo ra, trong khi biến `FILES` chỉ rõ file nào được chứa trong mỗi package,
 và được dùng để ghi đè cho package tương ứng. 
 Ví dụ, biến `FILES_${PN}` chỉ định rõ file nào sẽ đi vào package main ( ví dụ: package main được đặt tên theo tên của recipe luôn, trong đó biến `${`[`PN`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html
#var-PN)`}` để chỉ tên recipe). Thứ tự của các giá trị trong biến `PACKAGES` là có ý nghĩa nhất định. Với mỗi file cài đặt, chỉ giá trị biến `FILE` đầu tiên của package đó được matched. Mặc định thì `PACKAGES` và `FILES` sẽ luôn tồn tại. Vì thế, bạn hầu như không phải gán giá trị cho nó trừ khi phần mềm bạn đang build sẽ không được
cài đặt vào những chỗ thông thường.

## 2.7. Phục hồi thiết bị về trạng thái ban đầu 

 Nếu bạn sử dụng câu lệnh `devtool deploy-target` để ghi những kết quả vào target, 
 nơi có những thành phần đã tồn tại trước đó, sau đó bạn có thể rơi vào tình huống muốn phục hồi các trạng thái ngay trước khi chạy câu lệnh `devtool deploy-target`
. Bởi vì câu lệnh `devtool deploy-target` sẽ thực hiện back up bất cứ file nào nó định ghi đè, vì thế, vạn có thể sử dụng câu lệnh `devtool undeploy-target` để phục hồi các file đó và và loại bỏ các file đã được deploy.
 Hãy xem xét ví dụ dưới đây:

    
    
         $ devtool undeploy-target lighttpd root@192.168.7.2
                

 Nếu bạn đã deloy nhiều ứng dụng, bạn có thể sử dụng câu lệnh sau để gỡ bỏ tất
cả và đưa chúng về trạng thái ban đầu:

    
    
         $ devtool undeploy-target -a root@192.168.7.2
                

 Thông tin về các file được deployed và các file back up đều được lưu ở phía target
. Vì thế, nó sẽ chiếm thêm vùng lưu trữ trên target.

### Ghi chú 

 Câu lệnh `devtool deploy-target` và `devtool undeploy-target` không giao tiếp hay sử dụng bất cứ
chương trình quản lý gói nào trên target  (như RPM hoặc OPKG). Chính vì vậy, bạn không nên trộn lẫn các thao tác 
`devtool deploy-target` với các thao tác từ chương trình quản lý gói trên target.
  Làm vậy sẽ dẫn đến có thể dẫn đến những kết quả không mong muốn.

## 2.8. Cài đặt thêm cho SDK mở rộng 

 Một SDK mở rộng thường chỉ kèm theo một tập nhỏ các tool và thư viện mà thôi. 
 Nếu bạn có một SDK minimal, ban đầu chúng hầu như không có gì, mọi thứ được bung ra khi cần.
 Tuy nhiên, thỉnh thoảng bạn lại cần phải cài thêm một vài thứ cho SKD đấy. 
 Nếu bạn cần những thứ gì, đầu tiên hãy tìm kiếm chúng sử dụng câu lệnh `devtool search`. 
Ví dụ, bạn cần liên kết thư viện libGL bạn không biết chắc cái recipe nào chứa nó. 
 Bạn có thể giải quyết bằng câu lệnh dưới đây:

    
    
         $ devtool search libGL
         mesa                  A free implementation of the OpenGL API
                

 Một khi đã biết recipe nào ( ví dụ: trong ví dụ này là `mesa`), bạn có thể cài đặt nó như sau:

    
    
         $ devtool sdk-install mesa
                

 Mặc định, câu lệnh `devtool sdk-install` giả định rằng, item đã được build trước từ SDK provider. 
 Nếu nó có nhưng chưa được build trước, bạn cần build nó từ source, bằng cách thêm tham số "-s" như bên dưới đây:

    
    
         $ devtool sdk-install -s mesa
                

 Và nhớ rằng, bạn sẽ mất thời gian lâu hơn nhiều nếu build từ source
thay vì lấy từ kết quả đã build sẵn. Và nhớ rằng, nếu không tồn tại cái mà bạn đang tìm kiếm
để thêm vào SDK, bạn phải thêm nó bằng câu lệnh `devtool add` thôi.

## 2.9. Update SDK mở rộng

 Nếu bạn đang làm việc với một SDK mở rộng thì chúng sẽ thường được update thường xuyên (
thường thì SDK sẽ được cung cấp bởi một bên khác), bạn sẽ cần phải kéo các bản update
về cho SDK mà bạn đã cài.

 Để update SDK, sử dụng lệnh sau:

    
    
         $ devtool sdk-update
                

 Câu lệnh trên giả định rằng SDK provider có một tập các URL dành cho update rồi. 
 Nếu URL đó không được set, bạn sẽ cần phải set nó bằng câu lệnh kiểu như bên dưới đây:

    
    
         $ devtool sdk-update _path_to_update_directory_
                

### Ghi chú 

 URL này phải trỏ đến các published SDK và không phải cái bộ cài đặt SDK cái mà bạn
có thể tải về và cài đặt.

## 2.10. Tạo một SDK dẫn xuất từ các thành phần đang có 

 Bạn có thể tạo ra một SDK chứa các thư viện mà bạn đã custom cho bên thứ 3  ( ví dụ: bạn là một vender, bạn cung cấp cấp SDK cho khách hàng để họ build phần mềm trên platform đích chẳng hạn). Trong trường hợp đó, bạn có thể
tạo ra một SDK dẫn suất từ trạng thái hiện tại của bạn từ khá sớm. Sử dụng các bước dưới đây:

  1. Nếu cần, hãy cài một SDK mở rộng để làm base cho SDK dẫn suất. 

  2. Chạy script setup môi trường cho SDK. 

  3. Thêm thư viện, các component sử dụng câu lệnh `devtool add`.

  4. Chạy câu lệnh `devtool build-sdk`. 

 Câu lệnh trên sẽ lấy các recipe đã được thêm vào workspace để tạo ra một
new SDK installer chứa các recipe đó cũng như kết quả nhị phân của nó.
 Các recipe sẽ đứa chứa trong các layer của chúng in the constructed derivative
SDK, leaving the workspace clean and ready for users to add their own recipes.

## Chapter 3. Sử dụng Standard SDK

**Mục lục**

3.1. Tại sao sử dụng Standard SDK và Có gì trong đấy?

3.2. Cài đặt Standard SDK 

3.3. Chạy scrip setup môi trường 

 Chương này mô tả về Standard SDK và cài đặt nó. Information
includes unique installation and setup aspects for the standard SDK.

### Note

For a side-by-side comparison of main features supported for a standard SDK as
compared to an extensible SDK, see the "Introduction" section.

You can use a standard SDK to work on Makefile, Autotools, and Eclipse-based
projects. See the "Working with Different Types of Projects" chapter for more
information.

## 3.1. Why use the Standard SDK and What is in It?¶

The Standard SDK provides a cross-development toolchain and libraries tailored
to the contents of a specific image. You would use the Standard SDK if you
want a more traditional toolchain experience as compared to the extensible
SDK, which provides an internal build system and the `devtool` functionality.

The installed Standard SDK consists of several files and directories.
Basically, it contains an SDK environment setup script, some configuration
files, and host and target root filesystems to support usage. You can see the
directory structure in the "Installed Standard SDK Directory Structure"
section.

## 3.2. Installing the SDK¶

The first thing you need to do is install the SDK on your host development
machine by running the `*.sh` installation script.

You can download a tarball installer, which includes the pre-built toolchain,
the `runqemu` script, and support files from the appropriate directory under [
http://downloads.yoctoproject.org/releases/yocto/yocto-2.2/toolchain/](http://
downloads.yoctoproject.org/releases/yocto/yocto-2.2/toolchain/). Toolchains
are available for 32-bit and 64-bit x86 development systems from the `i686`
and `x86_64` directories, respectively. The toolchains the Yocto Project
provides are based off the `core-image-sato` image and contain libraries
appropriate for developing against that image. Each type of development system
supports five or more target architectures.

The names of the tarball installer scripts are such that a string representing
the host system appears first in the filename and then is immediately followed
by a string representing the target architecture.

    
    
         poky-glibc-_host_system_-_image_type_-_arch_-toolchain-_release_version_.sh
    
         Where:
             _host_system_ is a string representing your development system:
    
                        i686 or x86_64.
    
             _image_type_ is the image for which the SDK was built.
    
             _arch_ is a string representing the tuned target architecture:
    
                        i586, x86_64, powerpc, mips, armv7a or armv5te
    
             _release_version_ is a string representing the release number of the
                    Yocto Project:
    
                        2.2, 2.2+snapshot
                

For example, the following SDK installer is for a 64-bit development host
system and a i586-tuned target architecture based off the SDK for `core-image-
sato` and using the current 2.2 snapshot:

    
    
         poky-glibc-x86_64-core-image-sato-i586-toolchain-2.2.sh
                

### Note

As an alternative to downloading an SDK, you can build the SDK installer. For
information on building the installer, see the "Building an SDK Installer"
section. Another helpful resource for building an installer is the [Cookbook
guide to Making an Eclipse Debug Capable Image](https://wiki.yoctoproject.org/
wiki/TipsAndTricks/RunningEclipseAgainstBuiltImage) wiki page. This wiki page
focuses on development when using the Eclipse IDE.

The SDK and toolchains are self-contained and by default are installed into
`/opt/poky`. However, when you run the SDK installer, you can choose an
installation directory.

### Note

You must change the permissions on the SDK installer script so that it is
executable:

    
    
         $ chmod +x poky-glibc-x86_64-core-image-sato-i586-toolchain-2.2.sh
                    

The following command shows how to run the installer given a toolchain tarball
for a 64-bit x86 development host system and a 32-bit x86 target architecture.
The example assumes the SDK installer is located in `~/Downloads/`.

### Note

If you do not have write permissions for the directory into which you are
installing the SDK, the installer notifies you and exits. Be sure you have
write permissions in the directory and run the installer again.

    
    
         $ ./poky-glibc-x86_64-core-image-sato-i586-toolchain-2.2.sh
         Poky (Yocto Project Reference Distro) SDK installer version 2.2
         ===============================================================
         Enter target directory for SDK (default: /opt/poky/2.2):
         You are about to install the SDK to "/opt/poky/2.2". Proceed[Y/n]? Y
         Extracting SDK.......................................................................done
         Setting it up...done
         SDK has been successfully set up and is ready to be used.
         Each time you wish to use the SDK in a new shell session, you need to source the environment setup script e.g.
          $ . /opt/poky/2.2/environment-setup-i586-poky-linux
                

Again, reference the "Installed Standard SDK Directory Structure" section for
more details on the resulting directory structure of the installed SDK.

## 3.3. Running the SDK Environment Setup Script¶

Once you have the SDK installed, you must run the SDK environment setup script
before you can actually use it. This setup script resides in the directory you
chose when you installed the SDK. For information on where this setup script
can reside, see the "Obtaining the SDK" Appendix.

Before running the script, be sure it is the one that matches the architecture
for which you are developing. Environment setup scripts begin with the string
"`environment-setup`" and include as part of their name the tuned target
architecture. For example, the command to source a setup script for an IA-
based target machine using i586 tuning and located in the default SDK
installation directory is as follows:

    
    
         $ source /opt/poky/2.2/environment-setup-i586-poky-linux
                

When you run the setup script, the same environment variables are defined as
are when you run the setup script for an extensible SDK. See the "Running the
Extensible SDK Environment Setup Script" section for more information.

## Chapter 4. Using the SDK Toolchain Directly¶

**Table of Contents**

4.1. Autotools-Based Projects

    

4.1.1. Creating and Running a Project Based on GNU Autotools

4.1.2. Passing Host Options

4.2. Makefile-Based Projects

4.3. Developing Applications Using Eclipse™

    

4.3.1. Workflow Using Eclipse™

4.3.2. Working Within Eclipse

You can use the SDK toolchain directly with Makefile, Autotools, and Eclipse™
based projects. This chapter covers information specific to each of these
types of projects.

## 4.1. Autotools-Based Projects¶

Once you have a suitable cross-toolchain installed, it is very easy to develop
a project outside of the OpenEmbedded build system. This section presents a
simple "Helloworld" example that shows how to set up, compile, and run the
project.

### 4.1.1. Creating and Running a Project Based on GNU Autotools¶

Follow these steps to create a simple Autotools-based project:

  1. _Create your directory:_ Create a clean directory for your project and then make that directory your working location: 
    
    
         $ mkdir $HOME/helloworld
         $ cd $HOME/helloworld
                            

  2. _Populate the directory:_ Create `hello.c`, `Makefile.am`, and `configure.ac` files as follows: 

    * For `hello.c`, include these lines: 
    
    
         #include <stdio.h>
    
         main()
            {
               printf("Hello World!\n");
            }
                                    

    * For `Makefile.am`, include these lines: 
    
    
         bin_PROGRAMS = hello
         hello_SOURCES = hello.c
                                    

    * For `configure.in`, include these lines: 
    
    
         AC_INIT(hello,0.1)
         AM_INIT_AUTOMAKE([foreign])
         AC_PROG_CC
         AC_PROG_INSTALL
         AC_OUTPUT(Makefile)
                                    

  3. _Source the cross-toolchain environment setup file:_ As described earlier in the manual, installing the cross-toolchain creates a cross-toolchain environment setup script in the directory that the SDK was installed. Before you can use the tools to develop your project, you must source this setup script. The script begins with the string "environment-setup" and contains the machine architecture, which is followed by the string "poky-linux". Here is an example that sources a script from the default SDK installation directory that uses the 32-bit Intel x86 Architecture and the Morty Yocto Project release: 
    
    
         $ source /opt/poky/2.2/environment-setup-i586-poky-linux
                            

  4. _Generate the local aclocal.m4 files and create the configure script:_ The following GNU Autotools generate the local `aclocal.m4` files and create the configure script: 
    
    
         $ aclocal
         $ autoconf
                            

  5. _Generate files needed by GNU coding standards:_ GNU coding standards require certain files in order for the project to be compliant. This command creates those files: 
    
    
         $ touch NEWS README AUTHORS ChangeLog
                            

  6. _Generate the configure file:_ This command generates the `configure`: 
    
    
         $ automake -a
                            

  7. _Cross-compile the project:_ This command compiles the project using the cross-compiler. The [`CONFIGURE_FLAGS`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-CONFIGURE_FLAGS) environment variable provides the minimal arguments for GNU configure: 
    
    
         $ ./configure ${CONFIGURE_FLAGS}
                            

  8. _Make and install the project:_ These two commands generate and install the project into the destination directory: 
    
    
         $ make
         $ make install DESTDIR=./tmp
                            

  9. _Verify the installation:_ This command is a simple way to verify the installation of your project. Running the command prints the architecture on which the binary file can run. This architecture should be the same architecture that the installed cross-toolchain supports. 
    
    
         $ file ./tmp/usr/local/bin/hello
                            

  10. _Execute your project:_ To execute the project in the shell, simply enter the name. You could also copy the binary to the actual target hardware and run the project there as well: 
    
    
         $ ./hello
                            

As expected, the project displays the "Hello World!" message.

### 4.1.2. Passing Host Options¶

For an Autotools-based project, you can use the cross-toolchain by just
passing the appropriate host option to `configure.sh`. The host option you use
is derived from the name of the environment setup script found in the
directory in which you installed the cross-toolchain. For example, the host
option for an ARM-based target that uses the GNU EABI is `armv5te-poky-linux-
gnueabi`. You will notice that the name of the script is `environment-setup-
armv5te-poky-linux-gnueabi`. Thus, the following command works to update your
project and rebuild it using the appropriate cross-toolchain tools:

    
    
         $ ./configure --host=armv5te-poky-linux-gnueabi \
            --with-libtool-sysroot=_sysroot_dir_
                    

### Note

If the `configure` script results in problems recognizing the `--with-libtool-
sysroot=`_`sysroot-dir`_ option, regenerate the script to enable the support
by doing the following and then run the script again:

    
    
         $ libtoolize --automake
         $ aclocal -I ${OECORE_TARGET_SYSROOT}/usr/share/aclocal [-I _dir_containing_your_project-specific_m4_macros_]
         $ autoconf
         $ autoheader
         $ automake -a
                        

## 4.2. Makefile-Based Projects¶

For Makefile-based projects, the cross-toolchain environment variables
established by running the cross-toolchain environment setup script are
subject to general `make` rules.

To illustrate this, consider the following four cross-toolchain environment
variables:

    
    
         [CC](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-CC)=i586-poky-linux-gcc -m32 -march=i586 --sysroot=/opt/poky/2.2/sysroots/i586-poky-linux
         [LD](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-LD)=i586-poky-linux-ld --sysroot=/opt/poky/2.2/sysroots/i586-poky-linux
         [CFLAGS](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-CFLAGS)=-O2 -pipe -g -feliminate-unused-debug-types
         [CXXFLAGS](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-CXXFLAGS)=-O2 -pipe -g -feliminate-unused-debug-types
                

Now, consider the following three cases:

  * _Case 1 - No Variables Set in the `Makefile`:_ Because these variables are not specifically set in the `Makefile`, the variables retain their values based on the environment. 

  * _Case 2 - Variables Set in the `Makefile`:_ Specifically setting variables in the `Makefile` during the build results in the environment settings of the variables being overwritten. 

  * _Case 3 - Variables Set when the `Makefile` is Executed from the Command Line:_ Executing the `Makefile` from the command-line results in the variables being overwritten with command-line content regardless of what is being set in the `Makefile`. In this case, environment variables are not considered unless you use the "-e" flag during the build: 
    
    
         $ make -e _file_
                        

If you use this flag, then the environment values of the variables override
any variables specifically set in the `Makefile`.

### Note

For the list of variables set up by the cross-toolchain environment setup
script, see the "Running the SDK Environment Setup Script" section.

## 4.3. Developing Applications Using Eclipse™¶

If you are familiar with the popular Eclipse IDE, you can use an Eclipse Yocto
Plug-in to allow you to develop, deploy, and test your application all from
within Eclipse. This section describes general workflow using the SDK and
Eclipse and how to configure and set up Eclipse.

### 4.3.1. Workflow khi sử dụng Eclipse™

 Hình bên dưới và nội dung bên dưới mô tả ngắn gọn luồng phát triển ứng dụng nói
chung khi sử dụng cả 2 loại SDK trên Eclips:

![](figures/sdk-eclipse-dev-flow.png)

  1. _Chuẩn bị hệ thống host cho Yocto Project_: Xem thêm các chương "[Supported Linux Distributions](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#detailed-supported-distros)" và "[Required Packages for the Host Development System](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#required-packages-for-the-host-development-system)" trong tài liệu hướng dẫn tham khảo Yocto Project để biết thêm những yêu cầu cụ thể. Cần chắc chắn rằng trên hệ thống của bạn có gói `xterm` được cài đặt. 

  2. _ Làm việc với Yocto Project kernel target image_: Bạn phải có một ảnh của hệ thống đích, cái được build bởi OpenEmbedded build system.

 Phụ thuộc vào Yocto Project có sẵn ảnh hệ thống phù hợp với hệ thống đích của bạn hay không,
 rồi nơi bạn sẽ chạy ảnh hệ thống là gì (QEMU hay phần cứng thật), đây là những nơi bạn có thể tải ảnh về.

    * Tải từ [`machines`](http://downloads.yoctoproject.org/releases/yocto/yocto-2.2/machines) nếu kiến trúc của bạn được hỗ trợ và bạn có ý định phát triển và test ứng dụng trên phần cứng thật.

    * Tải từ [ `machines/qemu`](http://downloads.yoctoproject.org/releases/yocto/yocto-2.2/machines/qemu) nếu kiến trúc của bạn được hỗ trợ và bạn có ý định phát triển và test ứng dụng trên QEMU emulator. 

    * Hãy build một ảnh hệ thống nếu bạn không tìm thấy ảnh build sẵn phù hợp với kiến trúc của bạn. Nếu hệ thống của bạn tương tự một hệ thống được hỗ trợ, bạn có thể sửa kernel trước khi build nó. Xem phần chương "[Patching the Kernel](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#patching-the-kernel)" trong hướng dẫn phát triển Yocto Project Development để thấy ví dụ. 

  3. _Cài đặt SDK_: SDK cung cấp một toolchain cross-development cho target nhất định, hệ thống file root, QEMU emulator, và các tool khác phát triển ứng dụng dụng của mình. Thông tin về việc làm thế nào để cài đặt SDK, hãy xem thêm chương "Installing the SDK". 

  4. _ Hệ thống file root và toolchain Cross-development: Bạn cần tìm và tải hệ thống file root thích hợp cũng như toolchain cross-development.

 Bạn có thể tìm hệ thống file root ở cùng chỗ với ảnh kernel. Phụ thuộc vào loại ảnh hệ thống bạn đang chạy, hệ thống file root cũng khác nhau. Ví dụ , nếu bạn đang phát triển một ứng dụng hỗ trợ giao diện đồ họa Sato, thì bạn cũng cần một hệ thống file hỗ trợ Sato.

 Bạn có thể tìm một toolchain cross-development tại [`toolchains`](http://downloa
ds.yoctoproject.org/releases/yocto/yocto-2.2/toolchain/). Hãy chắc chắn rằng bạn tải
đúng toolchain phù hợp với hệ thống host và target của mình. Xem ở chương "Locating Pre-Built SDK Installers" và 
 chương "Installing the SDK" để biết thêm thông tin cài đặt.

### Ghi chú 

 Thay vì tải SDK về, bạn có thể tự build một bộ cài đặt SDK. Để biết thêm thông tin về một SDK như thế này,
xem ở chương "Building an SDK Installer"
. Một nơi khác cũng rất hữu ích để build một bộ cài đặt là trang wiki [Cookbook
guide to Making an Eclipse Debug Capable Image](https://wiki.yoctoproject.org/
wiki/TipsAndTricks/RunningEclipseAgainstBuiltImage).

  5. _ Tạo và build ứng dụng_: Đến điểm này rồi, bạn cần source cho ứng dụng của bạn. Khi đã có các file source rồi, bạn có thể sử dụng Eclipse IDE để import rồi build ứng dụng của bạn. Nếu không sử dụng Eclipse ID đi nữa, bạn sẽ cần các công cụ cross-development tools bạn đã cài đặt để tạo ảnh.

  6. _Triển khai ảnh có chứa ứng dụng_: Sử dụng IDE, bạn có thể triển khai ảnh hệ thống xuống phần cứng hoặc QEMU  thông qua thiết lập project. Bạn cũng có thể sử dụng Eclipse để load và test ứng dụng trên QEMU. Xem thê ở chapter "[Using the Quick EMUlator (QEMU)](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#dev-manual-qemu)" trong hướng dẫn phát triển Yocto Project Development Manual để biết thông tin sử dụng của QEMU. 

  7. _ Test và debug ứng dụng_: Khi ứng dụng đã được triển khai, bạn cần phải test nó. Bên trong Eclipse IDE, bạn có thể sử dụng môi trường debugging một loạt tool nâng cao hiệu năng được hỗ trợ [Linux Tools](http://www.eclipse.org/linuxtools/). 

### 4.3.2. Làm việc với Eclipse  IDE 

Eclipse IDE và một trường phát triển phổ biến, nó cũng hỗ trợ đầy đủ Yocto Project.

 Khi bạn cài đặt và sử dụng plugin Eclipse Yocto Project Plug-in vào 
Eclipse IDE, bạn có thể tận dụng tối đa khả năng của Yocto Project. Plugin này có những
có những extensions được thiết kế riêng giúp bạn dễ dàng hơn trong phát triển phần mềm.
. Những 
extensions cho phép cross-compilation, triển khai, chạy kết quả trên QEMU emulation sessionss cũng như
trên phần cứng thật. Bạn cũng có thể sử dụng cross-debugging và profiling. Môi trường này cũng có các
tool nâng cao hiệu năng nữa [tools](http://www.eclipse.org/linuxtools/) cho phép bạn thực hiện profiling, tracing, thu thập dữ liệu về nguồn, thu thập dữ liệu về độ trễ, thu thập dữ liệu về performance.

### Ghi chú 

 Phiên bản lần này của Yocto Project hỗ trợ cả phiên bản Neon and Mars của Eclipse IDE. 
 Chương này sẽ cung cấp các sử dụng Neon
 với Yocto Project. Thông tin về việc sử dụng phiên bản Mars của Eclipse với Yocto Project,
Xem thêm phần "Appendix C.

#### 4.3.2.1. Thiết lập cho phiên bản Neon của Eclipse IDE

 Để phát triển sử dụng Eclipse IDE, bạn cần đã những việc sau:

  1. Cài đặt phiên bản Neon của Eclipse IDE. 

  2. Cấu hình Eclipse IDE. 

  3. Cài đặt Plug-in Yocto cho Eclipse. 

  4. Cấu hình Plug-in Yocto cho Eclipse. 

### Ghi chú 

 Đừng cài đặt Eclipse từ kho phần mềm do distrobituon của bạn cung cấp. 
Hãy chắc chắn bạn cài Eclipse trang chủ của Eclipse bằng cách download trực tiếp.

##### 4.3.2.1.1. Cài đặt Eclipse Neon 

Follow these steps to locate, install, and configure Neon Eclipse:

  1. _Locate the Neon Download:_ Open a browser and go to [http://www.eclipse.org/neon/](http://www.eclipse.org/mars/). 

  2. _Download the Tarball:_ Click through the "Download" buttons to download the file. 

  3. _Unpack the Tarball:_ Move to a clean directory and unpack the tarball. Here is an example: 
    
    
         $ cd ~
         $ tar -xzvf ~/Downloads/eclipse-inst-linux64.tar.gz
                                    

Everything unpacks into a folder named "eclipse-installer".

  4. _Launch the Installer:_ Use the following commands to launch the installer: 
    
    
         $ cd ~/eclipse-installer
         $ ./eclipse-inst
                                    

  5. _Select Your IDE:_ From the list, select the "Eclipse IDE for C/C++ Developers". 

  6. _Install the Software:_ Accept the default "cpp-neon" directory and click "Install". Accept any license agreements and approve any certificates. 

  7. _Launch Neon:_ Click the "Launch" button and accept the default "workspace". 

##### 4.3.2.1.2. Configuring the Neon Eclipse IDE¶

Follow these steps to configure the Neon Eclipse IDE.

### Note

Depending on how you installed Eclipse and what you have already done, some of
the options will not appear. If you cannot find an option as directed by the
manual, it has already been installed.

  1. Be sure Eclipse is running and you are in your workbench. 

  2. Select "Install New Software" from the "Help" pull-down menu. 

  3. Select "Neon - http://download.eclipse.org/releases/neon" from the "Work with:" pull-down menu. 

  4. Expand the box next to "Linux Tools" and select the following: 
    
    
         C/C++ Remote (Over TCF/TE) Run/Debug Launcher
         TM Terminal
                                    

  5. Expand the box next to "Mobile and Device Development" and select the following boxes: 
    
    
         C/C++ Remote (Over TCF/TE) Run/Debug Launcher
         Remote System Explorer User Actions
         TM Terminal
         TCF Remote System Explorer add-in
         TCF Target Explorer
                                    

  6. Expand the box next to "Programming Languages" and select the following box: 
    
    
         C/C++ Development Tools SDK
                                    

  7. Complete the installation by clicking through appropriate "Next" and "Finish" buttons. 

##### 4.3.2.1.3. Cài đặt và sử dụng Plugin Yocto cho Neon Eclipse

 Bạn có thể cài đặt Plugin Yocto cho Eclipse bằng một trong 2 cách sau
: sử dụng trang update của chính Yocto Project dành cho Eclipse để tải bản Plug-in
được build sẵn
 hoặc build và cài đặt từ source mới nhất.

###### 4.3.2.1.3.1. Installing the Pre-built Plug-in from the Yocto Project
Eclipse Update Site¶

To install the Neon Eclipse Yocto Plug-in from the update site, follow these
steps:

  1. Start up the Eclipse IDE. 

  2. In Eclipse, select "Install New Software" from the "Help" menu. 

  3. Click "Add..." in the "Work with:" area. 

  4. Enter `http://downloads.yoctoproject.org/releases/eclipse-plugin/2.2/neon` in the URL field and provide a meaningful name in the "Name" field. 

  5. Click "OK" to have the entry added to the "Work with:" drop-down list. 

  6. Select the entry for the plug-in from the "Work with:" drop-down list. 

  7. Check the boxes next to the following: 
    
    
         Yocto Project SDK Plug-in
         Yocto Project Documentation plug-in
                                        

  8. Complete the remaining software installation steps and then restart the Eclipse IDE to finish the installation of the plug-in. 

### Note

You can click "OK" when prompted about installing software that contains
unsigned content.

###### 4.3.2.1.3.2. Installing the Plug-in Using the Latest Source Code¶

To install the Neon Eclipse Yocto Plug-in from the latest source code, follow
these steps:

  1. Be sure your development system has JDK 1.8+ 

  2. Install X11-related packages: 
    
    
         $ sudo apt-get install xauth
                                        

  3. In a new terminal shell, create a Git repository with: 
    
    
         $ cd ~
         $ git clone git://git.yoctoproject.org/eclipse-poky
                                        

  4. Use Git to create the correct tag: 
    
    
         $ cd ~/eclipse-poky
         $ git checkout neon/yocto-2.2
                                        

This creates a local tag named `neon/yocto-2.2` based on the branch `origin
/neon-master`. You are put into a detached HEAD state, which is fine since you
are only going to be building and not developing.

  5. Change to the `scripts` directory within the Git repository: 
    
    
         $ cd scripts
                                        

  6. Set up the local build environment by running the setup script: 
    
    
         $ ./setup.sh
                                        

When the script finishes execution, it prompts you with instructions on how to
run the `build.sh` script, which is also in the `scripts` directory of the Git
repository created earlier.

  7. Run the `build.sh` script as directed. Be sure to provide the tag name, documentation branch, and a release name. 

Following is an example:

    
    
         $ ECLIPSE_HOME=/home/scottrif/eclipse-poky/scripts/eclipse ./build.sh -l neon/yocto-2.2 master yocto-2.2 2>&1 | tee build.log
                                        

The previous example command adds the tag you need for `mars/yocto-2.2` to
`HEAD`, then tells the build script to use the local (-l) Git checkout for the
build. After running the script, the file
`org.yocto.sdk-`_`release`_`-`_`date`_`-archive.zip` is in the current
directory.

  8. If necessary, start the Eclipse IDE and be sure you are in the Workbench. 

  9. Select "Install New Software" from the "Help" pull-down menu. 

  10. Click "Add". 

  11. Provide anything you want in the "Name" field. 

  12. Click "Archive" and browse to the ZIP file you built earlier. This ZIP file should not be "unzipped", and must be the `*archive.zip` file created by running the `build.sh` script. 

  13. Click the "OK" button. 

  14. Check the boxes that appear in the installation window to install the following: 
    
    
         Yocto Project SDK Plug-in
         Yocto Project Documentation plug-in
                                        

  15. Finish the installation by clicking through the appropriate buttons. You can click "OK" when prompted about installing software that contains unsigned content. 

  16. Restart the Eclipse IDE if necessary. 

At this point you should be able to configure the Eclipse Yocto Plug-in as
described in the "Configuring the Neon Eclipse Yocto Plug-in" section.

##### 4.3.2.1.4. Configuring the Neon Eclipse Yocto Plug-in¶

 Cấu hình Neon Eclipse Yocto Plug-in đòi hỏi thiết lập tham số cho Cross Compiler
 và Target. Cấu hình bạn chọn sẽ trở thành mặc định cho tất cả các project của bạn. 
 Bạn không thể thay đổi chúng sau đó khi muốn cấu hình project ( Xem thêm ở chương bên dưới).

To start, you need to do the following from within the Eclipse IDE:

  * Choose "Preferences" from the "Window" menu to display the Preferences Dialog. 

  * Click "Yocto Project SDK" to display the configuration screen. 

The following sub-sections describe how to configure the plug-in.

### Ghi chú 

 Thông qua việc miêu tả, các ví dụ từ a đến z hướng dẫn đầy đủ để chuẩn bị ảnh
hệ thống dành cho QEMU khi sử dụng với Eclipse được miêu tả chi tiết ở đây trang wiki 
 [ Cookbook guide to Making an Eclipse Debug Capable Image](http
s://wiki.yoctoproject.org/wiki/TipsAndTricks/RunningEclipseAgainstBuiltImage)

###### 4.3.2.1.4.1. Cấu hình tham số của Cross-Compiler

 Việc cấu hình Cross Compiler cho phép Eclipse sử dụng cross compiler
toolchain. Để cấu hình những tham số này, bạn phải chọn loại toolchain,
 đường dẫn đến toolchain, chỉ định vị trí của sysroot, lựa chọn kiến trúc đích.

  * _Selecting the Toolchain Type:_Lựa chọn giữa `Standalone pre-built toolchain` và `Build system derived toolchain` là 2 option của Cross Compiler. 

    * _ `Standalone Pre-built Toolchain:` _ Chọn loại này, có nghĩa bạn sẽ sử dụng một stand-alone cross-toolchain. Ví dụ, giả sử bạn là developer phát triển ứng dụng, bạn không cần build build một ảnh hệ thống của target. Thay vào đó, bạn muốn sử dụng một toolchain cho kiến trúc cụ thể trên một kernel và một hệ thống file root sẵn có. Nói cách khác, bạn tải và cài đặt toolchain cho một ảnh hệ thống đã có sẵn. 

    * _ `Build System Derived Toolchain:` _ Chọn loại này, có nghĩa bạn muốn build một toolchain từ [Build Directory](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#build-directory). Khi bạn chọn `Build system derived toolchain`, bạn sẽ sử dụng toolchain được build bên dưới Build Directory. Ví dụ, giả sử bạn tạo một ảnh hệ thống theo từng bước giống như trang [wiki](https://wiki.yoctoproject.org/wiki/TipsAndTricks/RunningEclipseAgainstBuiltImage) này. Trong trường hợp này, bạn có thể chọn `Build system derived toolchain`. 

  * _Specify the Toolchain Root Location:_ Nếu bạn sẽ sử dụng một stand-alone toolchain được build sẵn rồi, bạn cần chỉ ra nơi nó được cài đặt ( ví dụ: `/opt/poky/2.2` chẳng hạn). Xem thêm ở chương "Installing the SDK" để biết thông tin về việc SDK được cài đặt như thế nào.

 Nếu bạn sử dụng toolchain từ build system (build system derived toolchain), đường dẫn bạn cung cấp cho trường `Toolchain Root Location` là [Build
Directory](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html
#build-directory) hay chính là nơi mà từ đó bạn chạy câu lệnh `bitbake`( ví dụ:
`/home/scottrif/poky/build`).

 Để xem thêm thông tin, bạn có thể xem chương "Building an SDK Installer".

  * _Specify Sysroot Location:_ Nơi chứa hệ thống file root chạy trên phần cứng. 

 Giá trị này phụ thuộc vào việc bạn có giải nén và cài đặt riêng cho hệ thống file root không . 
 Ví dụ, giả sử bạn đang chuẩn bị một ảnh hệ thống theo các bước trong trang này [wiki](https://wiki.yoctoproject.org/wiki/TipsAndTricks/RunningEc
lipseAgainstBuiltImage). Nếu vậy, thư mục `MY_QEMU_ROOTFS` bên dưới
[Build Directory](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-
manual.html#build-directory) bạn có thể mở browser và chọn thư mục đó 
(e.g. `/home/scottrif/poky/build/MY_QEMU_ROOTFS`).

 Thông tin về việc làm thế nào để cài đặt toolchain cũng như làm thế nào
để giải nén, cài đặt sysroot filesystem, có thể xem thêm tại chương "Building an SDK Installer".

  * _Select the Target Architecture:_ Kiến trúc là loại phần cứng mà bạn sẽ chạy hoặc giả lập. Chọn ở phần `Target Architecture` để đưa ra lựa chọn cho bạn. Những kiến trúc được hỗ trợ sẽ hiện ra trong menu chọn. Nếu kiến trúc của bạn không có trong menu, bạn cần phải build một ảnh hệ thống. Xem thêm ở chương "[Building Images](http://www.yoctoproject.org/docs/2.2/yocto-project-qs/yocto-project-qs.html#qs-building-images)" của hướng dẫn nhanh về Yocto Project Quick Start để có thêm thông tin. Bạn cũng có thể xem ở trang [wiki](https://wiki.yoctoproject.org/wiki/TipsAndTricks/RunningEclipseAgainstBuiltImage). 

###### 4.3.2.1.4.2. Cấu hình target 

 Bạn có thể chọn cách giả lập bằng QEMU emulator, hoặc chạy ảnh hệ thống trên một phần cứng thật.

  * _QEMU:_ Chọn option này nếu bạn muốn sử dụng QEMU emulator. Nếu bạn đang sử dụng QEMU Emulator, bạn cũng cần chỉ rõ chỗ chứa kernel cũng như các option khác.

 Nếu bạn đã chọn `Build system derived toolchain`, kernel dành cho target của bạn 
trong trường hợp này nằm ở [Build Directory](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html
#build-directory) với đường dẫn tương đối `tmp/deploy/images/_`machine`_`. Ví dụ,
 giả sử bạn đang thực hiện các step như trang [wiki](https://wiki.yoctoproject.org/wi
ki/TipsAndTricks/RunningEclipseAgainstBuiltImage) này. Trong trường hợp này, bạn chỉ định đường dẫn đến Build Directory kèm theo ảnh hệ thống  (e.g.
`/home/scottrif/poky/build/tmp/deploy/images/qemux86/bzImage-qemux86.bin`).

 Nếu bạn sử dụng một toolchain được build sẵn rồi, ảnh build sẵn của hệ thống 
được đặt ở thư mục mà bạn đã chỉ định khi tải chúng.

 Hầu hết các option nâng cao dành cho người dụng QEMU để giúp họ tùy chỉnh một QEMU instance. 
 Hầu hết option này được đặt trong một dấu nháy đơn.
 Một số khác được chỉ định bên ngoài. Cụ thể như, các option
 `serial`, `nographic`, and `kvm` phải được đặt bên ngoài. 
 Câu lệnh quen thuộc `man qemu` giúp bạn có thêm thông tin về các option và cách sử dụng chúng. 
 Dưới đây là một ví dụ:

    
    
        serial ‘<-m 256 -full-screen>’
                                        

 Bất kể bạn chọn mode nào, Sysroot luôn là một phần trong các option của Cross-
Compiler, bạn có thể thấy ở trường `Sysroot Location:`.

  * _External HW:_ Chọn giá trị này nếu bạn đang sử dụng phần cứng thật actual hardware.

Click the "Apply" and "OK" to save your plug-in configurations.

#### 4.3.2.2. Creating the Project¶

You can create two types of projects: Autotools-based, or Makefile-based. This
section describes how to create Autotools-based projects from within the
Eclipse IDE. For information on creating Makefile-based projects in a terminal
window, see the "Makefile-Based Projects" section.

### Note

Do not use special characters in project names (e.g. spaces, underscores,
etc.). Doing so can cause configuration to fail.

To create a project based on a Yocto template and then display the source
code, follow these steps:

  1. Select "C Project" from the "File -> New" menu. 

  2. Expand `Yocto Project SDK Autotools Project`. 

  3. Select `Hello World ANSI C Autotools Projects`. This is an Autotools-based project based on a Yocto template. 

  4. Put a name in the `Project name:` field. Do not use hyphens as part of the name (e.g. `hello`). 

  5. Click "Next". 

  6. Add appropriate information in the various fields. 

  7. Click "Finish". 

  8. If the "open perspective" prompt appears, click "Yes" so that you in the C/C++ perspective. 

  9. The left-hand navigation pane shows your project. You can display your source by double clicking the project's source file. 

#### 4.3.2.3. Cấu hình Cross-Toolchains

The earlier section, "Configuring the Neon Eclipse Yocto Plug-in", sets up the
default project configurations. You can override these settings for a given
project by following these steps:

  1. Select "Yocto Project Settings" from the "Project -> Properties" menu. This selection brings up the Yocto Project Settings Dialog and allows you to make changes specific to an individual project.

By default, the Cross Compiler Options and Target Options for a project are
inherited from settings you provided using the Preferences Dialog as described
earlier in the "Configuring the Neon Eclipse Yocto Plug-in" section. The Yocto
Project Settings Dialog allows you to override those default settings for a
given project.

  2. Make or verify your configurations for the project and click "OK". 

  3. Right-click in the navigation pane and select "Reconfigure Project" from the pop-up menu. This selection reconfigures the project by running `autogen.sh` in the workspace for your project. The script also runs `libtoolize`, `aclocal`, `autoconf`, `autoheader`, `automake --a`, and `./configure`. Click on the "Console" tab beneath your source code to see the results of reconfiguring your project. 

#### 4.3.2.4. Building the Project¶

To build the project select "Build All" from the "Project" menu. The console
should update and you can note the cross-compiler you are using.

### Note

When building "Yocto Project SDK Autotools" projects, the Eclipse IDE might
display error messages for Functions/Symbols/Types that cannot be "resolved",
even when the related include file is listed at the project navigator and when
the project is able to build. For these cases only, it is recommended to add a
new linked folder to the appropriate sysroot. Use these steps to add the
linked folder:

  1. Select the project. 

  2. Select "Folder" from the `File > New` menu. 

  3. In the "New Folder" Dialog, select "Link to alternate location (linked folder)". 

  4. Click "Browse" to navigate to the include folder inside the same sysroot location selected in the Yocto Project configuration preferences. 

  5. Click "OK". 

  6. Click "Finish" to save the linked folder. 

#### 4.3.2.5. Sử dụng QEMU trong User-Space NFS Mode
 
Để bắt đầu sử dụng QEMU emulator trên Eclipse, hãy thực hiện các bước sau:

### Ghi chú 

 Xem thêm ở chapter "[Using the Quick EMUlator
(QEMU)](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#dev-
manual-qemu)" trong hướng dẫn phát triển Yocto Project Development
để biết thêm thông tin khi sử dụng QEMU.

  1. Tìm đến mục "External Tools Configurations ..." từ menu "Run -> External Tools". 

  2. Xác định và chọn ảnh ở panel bên trái ( ví dụ:`qemu_i586-poky-linux`). 

  3. Click vào "Run" để chạy QEMU. 

### Ghi chú 

 Máy host mà bạn đang chạy QEMU phải có tiện ích `rpcbind` được chạy sẵn 
 thì mới có thể thực hiện lời gọi RPC trên server ở máy QEMU được. Nếu QEMU
không bật lên được và hiện ra thông báo lỗi liên quan đến `rpcbind`, 
Hãy theo dõi những gợi ý sau để thực hiện việc chạy nó. Ví dụ trên môi trường Ubuntu 16.04
LTS, bạn có thể thực hiện các bước sau để chạy QEMU:

    
    
         $ sudo apt-get install rpcbind
                                    

 Sau khi cài đặt `rpcbind` rồi, bạn cần sửa lại file `/etc/init.d/rpcbind` theo cách sau:

    
    
         OPTIONS="-i -w"
                                    

Sau khi sửa xong, bạn cần restart lại dịch vụ:

    
    
         $ sudo service portmap restart
                                    

  4. Nếu cần, bạn có khi phải gõ mật khẩu vào shell. Cái này sẽ thực hiện thiết lập kết nối `Tap 0` connection cần thiết cho việc chạy user-space NFS mode. 

  5. Đợi đến khi QEMU chạy ở chế độ user-space NFS 

  6. Khi QEMU đã chạy lên được rồi, bạn có thể thao tác với môi trường đó được rồi. Nhiệm vụ đầu tiên là xác định IP của user-space NFS bằng cách sử dụng câu lệnh quen thuộc `ifconfig`. IP của máy QEMU sẽ xuất hiện ở màn hình xterm. Bạn có thể dùng IP ở những mà địa chỉ IP của QEMU đang được sử dụng trong thiết lập. 

#### 4.3.2.6. Triển khai và debug ứng dụng 

 Một khi bạn có QEMU chạy một ảnh hệ thống rồi, bạn có thể triển khai ứng dụng sử dụng 
Eclipse IDE sau đó sử dụng emulator để thực hiện debug. Làm theo các bước sau để triển khai ứng dụng.

### Ghi chú 
 
 Hiện tại, Eclipse IDE không hỗ trợ SSH port forwarding. Chính vì thế, nếu bạn muốn chạy và 
debug ứng dụng trên máy host, bạn phải tạo một kết  
 từ bên ngoài Eclipse và giữ kết nối đó trong suốt quá trình làm việc. 
 Ví dụ, trên terminal bạn chạy lệnh sau:

    
    
         $ ssh -XY _user_name_@_remote_host_ip_
                            

 Với dạng sử dụng như trên, ta có ví dụ như sau:

    
    
         $ ssh -XY root@192.168.7.2
                            

 Sau khi chạy câu lệnh trên, thêm command sau vào phần cấu hình chạy của Eclipse
 trước khi chạy ứng dụng:


    
         export DISPLAY=:10.0
                            

 Hãy chắc chắn không phá hủy kết nối trong suốt QEMU session ( ví dụ: đừng thoát khỏi shell).

  1. Chọn "Debug Configurations..." từ menu "Run". 

  2. Mở rộng chỗ `C/C++Remote Application`. 

  3. Locate your project and select it to bring up a new tabbed view in the Debug Configurations Dialog. 

  4. Click on the "Debugger" tab to see the cross-tool debugger you are using. Be sure to change to the debugger perspective in Eclipse. 

  5. Click on the "Main" tab. 

  6. Create a new connection to the QEMU instance by clicking on "new".

  7. Select `SSH`, which means Secure Socket Shell and then click "OK". Optionally, you can select an TCF connection instead. 

  8. Clear out the "Connection name" field and enter any name you want for the connection. 

  9. Put the IP address for the connection in the "Host" field. For QEMU, the default is `192.168.7.2`. However, if a previous QEMU session did not exit cleanly, the IP address increments (e.g. `192.168.7.3`). 

### Note

You can find the IP address for the current QEMU session by looking in the
xterm that opens when you launch QEMU.

  10. Enter `root`, which is the default for QEMU, for the "User" field. Be sure to leave the password field empty. 

  11. Click "Finish" to close the New Connections Dialog. 

  12. If necessary, use the drop-down menu now in the "Connection" field and pick the IP Address you entered. 

  13. Assuming you are connecting as the root user, which is the default for QEMU x86-64 SDK images provided by the Yocto Project, in the "Remote Absolute File Path for C/C++ Application" field, browse to `/home/root/`_`ProjectName`_ (e.g. `/home/root/hello`). You could also browse to any other path you have write access to on the target such as `/usr/bin`. This location is where your application will be located on the QEMU system. If you fail to browse to and specify an appropriate location, QEMU will not understand what to remotely launch. Eclipse is helpful in that it auto fills your application name for you assuming you browsed to a directory. 

### Note

If you are prompted to provide a username and to optionally set a password, be
sure you provide "root" as the username and you leave the password field
blank.

  14. Be sure you change to the "Debug" perspective in Eclipse. 

  15. Click "Debug" 

  16. Accept the debug perspective. 

#### 4.3.2.7. Using Linuxtools¶

As mentioned earlier in the manual, performance tools exist (Linuxtools) that
enhance your development experience. These tools are aids in developing and
debugging applications and images. You can run these tools from within the
Eclipse IDE through the "Linuxtools" menu.

For information on how to configure and use these tools, see
[http://www.eclipse.org/linuxtools/](http://www.eclipse.org/linuxtools/).

## Appendix A. Obtaining the SDK¶

**Table of Contents**

A.1. Locating Pre-Built SDK Installers

A.2. Building an SDK Installer

A.3. Extracting the Root Filesystem

A.4. Installed Standard SDK Directory Structure

A.5. Installed Extensible SDK Directory Structure

## A.1. Locating Pre-Built SDK Installers¶

You can use existing, pre-built toolchains by locating and running an SDK
installer script that ships with the Yocto Project. Using this method, you
select and download an architecture-specific SDK installer and then run the
script to hand-install the toolchain.

You can find SDK installers here:

  * _Standard SDK Installers:_ Go to [http://downloads.yoctoproject.org/releases/yocto/yocto-2.2/toolchain/](http://downloads.yoctoproject.org/releases/yocto/yocto-2.2/toolchain/) and find the folder that matches your host development system (i.e. `i686` for 32-bit machines or `x86_64` for 64-bit machines).

Go into that folder and download the SDK installer whose name includes the
appropriate target architecture. The toolchains provided by the Yocto Project
are based off of the `core-image-sato` image and contain libraries appropriate
for developing against that image. For example, if your host development
system is a 64-bit x86 system and you are going to use your cross-toolchain
for a 32-bit x86 target, go into the `x86_64` folder and download the
following installer:

    
    
         poky-glibc-x86_64-core-image-sato-i586-toolchain-2.2.sh
                    

  * _Extensible SDK Installers:_ Installers for the extensible SDK are also located in [http://downloads.yoctoproject.org/releases/yocto/yocto-2.2/toolchain/](http://downloads.yoctoproject.org/releases/yocto/yocto-2.2/toolchain/). These installers have the string `ext` as part of their names: 
    
    
         poky-glibc-x86_64-core-image-sato-core2-64-toolchain-ext-2.2.sh
                    

## A.2. Building an SDK Installer¶

As an alternative to locating and downloading a SDK installer, you can build
the SDK installer assuming you have first sourced the environment setup
script. See the "[Building Images](http://www.yoctoproject.org/docs/2.2/yocto-
project-qs/yocto-project-qs.html#qs-building-images)" section in the Yocto
Project Quick Start for steps that show you how to set up the Yocto Project
environment. In particular, you need to be sure the
[`MACHINE`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html
#var-MACHINE) variable matches the architecture for which you are building and
that the [`SDKMACHINE`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-
manual.html#var-SDKMACHINE) variable is correctly set if you are building a
toolchain designed to run on an architecture that differs from your current
development host machine (i.e. the build machine).

To build the SDK installer for a standard SDK and populate the SDK image, use
the following command:

    
    
         $ bitbake _image_ -c populate_sdk
            

You can do the same for the extensible SDK using this command:

    
    
         $ bitbake _image_ -c populate_sdk_ext
            

These commands result in a SDK installer that contains the sysroot that
matches your target root filesystem.

When the `bitbake` command completes, the SDK installer will be in
`tmp/deploy/sdk` in the Build Directory.

### Notes

  * By default, this toolchain does not build static binaries. If you want to use the toolchain to build these types of libraries, you need to be sure your image has the appropriate static development libraries. Use the [`IMAGE_INSTALL`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-IMAGE_INSTALL) variable inside your `local.conf` file to install the appropriate library packages. Following is an example using `glibc` static development libraries: 
    
    
         IMAGE_INSTALL_append = " glibc-staticdev"
                        

  * For additional information on building the installer, see the [Cookbook guide to Making an Eclipse Debug Capable Image](https://wiki.yoctoproject.org/wiki/TipsAndTricks/RunningEclipseAgainstBuiltImage) wiki page. 

## A.3. Extracting the Root Filesystem¶

 Sau khi đã cài Toolchain rồi, thỉnh thoảng bạn có thể cần giải nén root file system:

  * Bạn muốn boot sử dụng NFS chẳng hạn. 

  * Bạn muốn sử dụng một root filesystem giống target. Ví dụ, IDE Eclipse mà được cài Yocto Plug-in cho phép sử dụng QEMU để build qua NFS.

  * Nếu bạn muốn phát triển ứng dụng sử dụng root filesystem như trên target sysroot. 

To extract the root filesystem, first `source` the cross-development
environment setup script to establish necessary environment variables. If you
built the toolchain in the Build Directory, you will find the toolchain
environment script in the `tmp` directory. If you installed the toolchain by
hand, the environment setup script is located in `/opt/poky/2.2`.

After sourcing the environment script, use the `runqemu-extract-sdk` command
and provide the filesystem image.

Following is an example. The second command sets up the environment. In this
case, the setup script is located in the `/opt/poky/2.2` directory. The third
command extracts the root filesystem from a previously built filesystem that
is located in the `~/Downloads` directory. Furthermore, this command extracts
the root filesystem into the `qemux86-sato` directory:

    
    
         $ cd ~
         $ source /opt/poky/2.2/environment-setup-i586-poky-linux
         $ runqemu-extract-sdk \
            ~/Downloads/core-image-sato-sdk-qemux86-2011091411831.rootfs.tar.bz2 \
            $HOME/qemux86-sato
            

You could now point to the target sysroot at `qemux86-sato`.

## A.4. Installed Standard SDK Directory Structure¶

The following figure shows the resulting directory structure after you install
the Standard SDK by running the `*.sh` SDK installation script:

![](figures/sdk-installed-standard-sdk-directory.png)

The installed SDK consists of an environment setup script for the SDK, a
configuration file for the target, a version file for the target, and the root
filesystem (`sysroots`) needed to develop objects for the target system.

Within the figure, italicized text is used to indicate replaceable portions of
the file or directory name. For example, _`install_dir`_/_`version`_ is the
directory where the SDK is installed. By default, this directory is
`/opt/poky/`. And, _`version`_ represents the specific snapshot of the SDK
(e.g. `2.2`). Furthermore, _`target`_ represents the target architecture (e.g.
`i586`) and _`host`_ represents the development system's architecture (e.g.
`x86_64`). Thus, the complete names of the two directories within the
`sysroots` could be `i586-poky-linux` and `x86_64-pokysdk-linux` for the
target and host, respectively.

## A.5. Installed Extensible SDK Directory Structure¶

The following figure shows the resulting directory structure after you install
the Extensible SDK by running the `*.sh` SDK installation script:

![](figures/sdk-installed-extensible-sdk-directory.png)

The installed directory structure for the extensible SDK is quite different
than the installed structure for the standard SDK. The extensible SDK does not
separate host and target parts in the same manner as does the standard SDK.
The extensible SDK uses an embedded copy of the OpenEmbedded build system,
which has its own sysroots.

Of note in the directory structure are an environment setup script for the
SDK, a configuration file for the target, a version file for the target, and a
log file for the OpenEmbedded build system preparation script run by the
installer.

Within the figure, italicized text is used to indicate replaceable portions of
the file or directory name. For example, _`install_dir`_ is the directory
where the SDK is installed, which is `poky_sdk` by default. _`target`_
represents the target architecture (e.g. `i586`) and _`host`_ represents the
development system's architecture (e.g. `x86_64`).

## Appendix B. Customizing the Extensible SDK¶

**Table of Contents**

B.1. Configuring the Extensible SDK

B.2. Adjusting the Extensible SDK to Suit Your Build System Setup

B.3. Changing the Appearance of the Extensible SDK

B.4. Providing Updates After Installing the Extensible SDK

B.5. Providing Additional Installable Extensible SDK Content

B.6. Minimizing the Size of the Extensible SDK Installer Download

This appendix presents customizations you can apply to the extensible SDK.

## B.1. Configuring the Extensible SDK¶

The extensible SDK primarily consists of a pre-configured copy of the
OpenEmbedded build system from which it was produced. Thus, the SDK's
configuration is derived using that build system and the following filters,
which the OpenEmbedded build system applies against `local.conf` and
`auto.conf` if they are present:

  * Variables whose values start with "/" are excluded since the assumption is that those values are paths that are likely to be specific to the build host. 

  * Variables listed in [`SDK_LOCAL_CONF_BLACKLIST`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-SDK_LOCAL_CONF_BLACKLIST) are excluded. The default value blacklists [`CONF_VERSION`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-CONF_VERSION), [`BB_NUMBER_THREADS`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-BB_NUMBER_THREADS), [`PARALLEL_MAKE`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-PARALLEL_MAKE), [`PRSERV_HOST`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-PRSERV_HOST), and [`SSTATE_MIRRORS`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-SSTATE_MIRRORS). 

  * Variables listed in [`SDK_LOCAL_CONF_WHITELIST`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-SDK_LOCAL_CONF_WHITELIST) are included. Including a variable in the value of `SDK_LOCAL_CONF_WHITELIST` overrides either of the above two conditions. The default value is blank. 

  * Classes inherited globally with [`INHERIT`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-INHERIT) that are listed in [`SDK_INHERIT_BLACKLIST`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-SDK_INHERIT_BLACKLIST) are disabled. Using `SDK_INHERIT_BLACKLIST` to disable these classes is is the typical method to disable classes that are problematic or unnecessary in the SDK context. The default value blacklists the [`buildhistory`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#ref-classes-buildhistory) and [`icecc`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#ref-classes-icecc) classes. 

Additionally, the contents of `conf/sdk-extra.conf`, when present, are
appended to the end of `conf/local.conf` within the produced SDK, without any
filtering. The `sdk-extra.conf` file is particularly useful if you want to set
a variable value just for the SDK and not the OpenEmbedded build system used
to create the SDK.

## B.2. Adjusting the Extensible SDK to Suit Your Build System Setup¶

In most cases, the extensible SDK defaults should work. However, some cases
exist for which you might consider making adjustments:

  * If your SDK configuration inherits additional classes using the [`INHERIT`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-INHERIT) variable and you do not need or want those classes enabled in the SDK, you can blacklist them by adding them to the [`SDK_INHERIT_BLACKLIST`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-SDK_INHERIT_BLACKLIST) variable. The default value of `SDK_INHERIT_BLACKLIST` is set using the "?=" operator. Consequently, you will need to either set the complete value using "=" or append the value using "_append". 

  * If you have classes or recipes that add additional tasks to the standard build flow (i.e. that execute as part of building the recipe as opposed to needing to be called explicitly), then you need to do one of the following: 

    * Ensure the tasks are shared state tasks (i.e. their output is saved to and can be restored from the shared state cache), or that the tasks are able to be produced quickly from a task that is a shared state task and add the task name to the value of [`SDK_RECRDEP_TASKS`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-SDK_RECRDEP_TASKS). 

    * Disable the tasks if they are added by a class and you do not need the functionality the class provides in the extensible SDK. To disable the tasks, add the class to `SDK_INHERIT_BLACKLIST` as previously described. 

  * Generally, you want to have a shared state mirror set up so users of the SDK can add additional items to the SDK after installation without needing to build the items from source. See the "Providing Additional Installable Extensible SDK Content" section for information. 

  * If you want users of the SDK to be able to easily update the SDK, you need to set the [`SDK_UPDATE_URL`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-SDK_UPDATE_URL) variable. For more information, see the "Providing Updates After Installing the Extensible SDK" section. 

  * If you have adjusted the list of files and directories that appear in [`COREBASE`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-COREBASE) (other than layers that are enabled through `bblayers.conf`), then you must list these files in [`COREBASE_FILES`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-COREBASE_FILES) so that the files are copied into the SDK. 

  * If your OpenEmbedded build system setup uses a different environment setup script other than [`oe-init-build-env`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#structure-core-script) or [`oe-init-build-env-memres`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#structure-memres-core-script), then you must set [`OE_INIT_ENV_SCRIPT`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-OE_INIT_ENV_SCRIPT) to point to the environment setup script you use. 

### Note

You must also reflect this change in the value used for the `COREBASE_FILES`
variable as previously described.

## B.3. Changing the Appearance of the Extensible SDK¶

You can change the title shown by the SDK installer by setting the
[`SDK_TITLE`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html
#var-SDK_TITLE) variable. By default, this title is derived from
[`DISTRO_NAME`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-
manual.html#var-DISTRO_NAME) when it is set. If the `DISTRO_NAME` variable is
not set, the title is derived from the
[`DISTRO`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html
#var-DISTRO) variable.

## B.4. Providing Updates After Installing the Extensible SDK¶

When you make changes to your configuration or to the metadata and if you want
those changes to be reflected in installed SDKs, you need to perform
additional steps to make it possible for those that use the SDK to update
their installations with the `devtool sdk-update` command:

  1. Arrange to be created a directory that can be shared over HTTP or HTTPS. 

  2. Set the [`SDK_UPDATE_URL`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-SDK_UPDATE_URL) variable to point to the corresponding HTTP or HTTPS URL. Setting this variable causes any SDK built to default to that URL and thus, the user does not have to pass the URL to the `devtool sdk-update` command. 

  3. Build the extensible SDK normally (i.e., use the `bitbake -c populate_sdk_ext` _`imagename`_ command). 

  4. Publish the SDK using the following command: 
    
    
         $ oe-publish-sdk _some_path_/sdk-installer.sh _path_to_shared/http_directory_
                    

You must repeat this step each time you rebuild the SDK with changes that you
want to make available through the update mechanism.

Completing the above steps allows users of the existing SDKs to simply run
`devtool sdk-update` to retrieve the latest updates. See the "Updating the
Extensible SDK" section for further information.

## B.5. Providing Additional Installable Extensible SDK Content¶

If you want the users of the extensible SDK you are building to be able to add
items to the SDK without needing to build the items from source, you need to
do a number of things:

  1. Ensure the additional items you want the user to be able to install are actually built. You can ensure these items are built a number of different ways: 1) Build them explicitly, perhaps using one or more "meta" recipes that depend on lists of other recipes to keep things tidy, or 2) Build the "world" target and set `EXCLUDE_FROM_WORLD_pn-`_`recipename`_ for the recipes you do not want built. See the [`EXCLUDE_FROM_WORLD`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-EXCLUDE_FROM_WORLD) variable for additional information. 

  2. Expose the `sstate-cache` directory produced by the build. Typically, you expose this directory over HTTP or HTTPS. 

  3. Set the appropriate configuration so that the produced SDK knows how to find the configuration. The variable you need to set is [`SSTATE_MIRRORS`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-SSTATE_MIRRORS): 
    
    
         SSTATE_MIRRORS = "file://.*  http://_example_.com/_some_path_/sstate-cache/PATH"
                    

You can set the `SSTATE_MIRRORS` variable in two different places:

    * If the mirror value you are setting is appropriate to be set for both the OpenEmbedded build system that is actually building the SDK and the SDK itself (i.e. the mirror is accessible in both places or it will fail quickly on the OpenEmbedded build system side, and its contents will not interfere with the build), then you can set the variable in your `local.conf` or custom distro configuration file. You can then "whitelist" the variable through to the SDK by adding the following: 
    
    
         SDK_LOCAL_CONF_WHITELIST = "SSTATE_MIRRORS"
                            

    * Alternatively, if you just want to set the `SSTATE_MIRRORS` variable's value for the SDK alone, create a `conf/sdk-extra.conf` either in your [Build Directory](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#build-directory) or within any layer and put your `SSTATE_MIRRORS` setting within that file. 

### Note

This second option is the safest option should you have any doubts as to which
method to use when setting `SSTATE_MIRRORS`.

## B.6. Minimizing the Size of the Extensible SDK Installer Download¶

By default, the extensible SDK bundles the shared state artifacts for
everything needed to reconstruct the image for which the SDK was built. This
bundling can lead to an SDK installer file that is a Gigabyte or more in size.
If the size of this file causes a problem, you can build an SDK that has just
enough in it to install and provide access to the `devtool command` by setting
the following in your configuration:

    
    
         SDK_EXT_TYPE = "minimal"
            

Setting [`SDK_EXT_TYPE`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-
manual.html#var-SDK_EXT_TYPE) to "minimal" produces an SDK installer that is
around 35 Mbytes in size, which downloads and installs quickly. You need to
realize, though, that the minimal installer does not install any libraries or
tools out of the box. These must be installed either "on the fly" or through
actions you perform using `devtool` or explicitly with the `devtool sdk-
install` command.

In most cases, when building a minimal SDK you will need to also enable
bringing in the information on a wider range of packages produced by the
system. This is particularly true so that `devtool add` is able to effectively
map dependencies it discovers in a source tree to the appropriate recipes.
Also so that the `devtool search` command is able to return useful results.

To facilitate this wider range of information, you would additionally set the
following:

    
    
         SDK_INCLUDE_PKGDATA = "1"
            

See the [`SDK_INCLUDE_PKGDATA`](http://www.yoctoproject.org/docs/2.2/ref-
manual/ref-manual.html#var-SDK_INCLUDE_PKGDATA) variable for additional
information.

Setting the `SDK_INCLUDE_PKGDATA` variable as shown causes the "world" target
to be built so that information for all of the recipes included within it are
available. Having these recipes available increases build time significantly
and increases the size of the SDK installer by 30-80 Mbytes depending on how
many recipes are included in your configuration.

You can use `EXCLUDE_FROM_WORLD_pn-`_`recipename`_ for recipes you want to
exclude. However, it is assumed that you would need to be building the "world"
target if you want to provide additional items to the SDK. Consequently,
building for "world" should not represent undue overhead in most cases.

### Note

If you set `SDK_EXT_TYPE` to "minimal", then providing a shared state mirror
is mandatory so that items can be installed as needed. See the "Providing
Additional Installable Extensible SDK Content" section for more information.

You can explicitly control whether or not to include the toolchain when you
build an SDK by setting the
[`SDK_INCLUDE_TOOLCHAIN`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-
manual.html#var-SDK_INCLUDE_TOOLCHAIN) variable to "1". In particular, it is
useful to include the toolchain when you have set `SDK_EXT_TYPE` to "minimal",
which by default, excludes the toolchain. Also, it is helpful if you are
building a small SDK for use with an IDE, such as Eclipse, or some other tool
where you do not want to take extra steps to install a toolchain.

## Appendix C. Customizing the Standard SDK¶

**Table of Contents**

C.1. Adding Individual Packages to the Standard SDK

C.2. Adding API Documentation to the Standard SDK

This appendix presents customizations you can apply to the standard SDK.

## C.1. Adding Individual Packages to the Standard SDK¶

When you build a standard SDK using the `bitbake -c populate_sdk`, a default
set of packages is included in the resulting SDK. The
[`TOOLCHAIN_HOST_TASK`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-
manual.html#var-TOOLCHAIN_HOST_TASK) and
[`TOOLCHAIN_TARGET_TASK`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-
manual.html#var-TOOLCHAIN_TARGET_TASK) variables control the set of packages
adding to the SDK.

If you want to add individual packages to the toolchain that runs on the host,
simply add those packages to the `TOOLCHAIN_HOST_TASK` variable. Similarly, if
you want to add packages to the default set that is part of the toolchain that
runs on the target, add the packages to the `TOOLCHAIN_TARGET_TASK` variable.

## C.2. Adding API Documentation to the Standard SDK¶

You can include API documentation as well as any other documentation provided
by recipes with the standard SDK by adding "api-documentation" to the
[`DISTRO_FEATURES`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-
manual.html#var-DISTRO_FEATURES) variable:

    
    
         DISTRO_FEATURES_append = " api-documentation"
            

Setting this variable as shown here causes the OpenEmbedded build system to
build the documentation and then include it in the standard SDK.

## Appendix D. Using Eclipse Mars¶

**Table of Contents**

D.1. Setting Up the Mars Version of the Eclipse IDE

    

D.1.1. Installing the Mars Eclipse IDE

D.1.2. Configuring the Mars Eclipse IDE

D.1.3. Installing or Accessing the Mars Eclipse Yocto Plug-in

D.1.4. Configuring the Mars Eclipse Yocto Plug-in

D.2. Creating the Project

D.3. Configuring the Cross-Toolchains

D.4. Building the Project

D.5. Starting QEMU in User-Space NFS Mode

D.6. Deploying and Debugging the Application

D.7. Using Linuxtools

This release of the Yocto Project supports both the Neon and Mars versions of
the Eclipse IDE. This appendix presents information that describes how to
obtain and configure the Mars version of Eclipse. It also provides a basic
project example that you can work through from start to finish. For general
information on using the Eclipse IDE and the Yocto Project Eclipse Plug-In,
see the "Developing Applications Using Eclipse™" section.

## D.1. Setting Up the Mars Version of the Eclipse IDE¶

To develop within the Eclipse IDE, you need to do the following:

  1. Install the Mars version of the Eclipse IDE.

  2. Configure the Eclipse IDE. 

  3. Install the Eclipse Yocto Plug-in. 

  4. Configure the Eclipse Yocto Plug-in. 

### Note

Do not install Eclipse from your distribution's package repository. Be sure to
install Eclipse from the official Eclipse download site as directed in the
next section.

### D.1.1. Installing the Mars Eclipse IDE¶

Follow these steps to locate, install, and configure Mars Eclipse:

  1. _Locate the Mars Download:_ Open a browser and go to [http://www.eclipse.org/mars/](http://www.eclipse.org/mars/). 

  2. _Download the Tarball:_ Click the "Download" button and then use the "Linux for Eclipse IDE for C++ Developers" appropriate for your development system (e.g. [64-bit under Linux for Eclipse IDE for C++ Developers](http://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/mars/2/eclipse-cpp-mars-2-linux-gtk-x86_64.tar.gz) if your development system is a Linux 64-bit machine. 

  3. _Unpack the Tarball:_ Move to a clean directory and unpack the tarball. Here is an example: 
    
    
         $ cd ~
         $ tar -xzvf ~/Downloads/eclipse-cpp-mars-2-linux-gtk-x86_64.tar.gz
                            

Everything unpacks into a folder named "Eclipse".

  4. _Launch Eclipse:_ Double click the "Eclipse" file in the folder to launch Eclipse. 

### D.1.2. Configuring the Mars Eclipse IDE¶

Follow these steps to configure the Mars Eclipse IDE.

### Note

Depending on how you installed Eclipse and what you have already done, some of
the options will not appear. If you cannot find an option as directed by the
manual, it has already been installed.

  1. Be sure Eclipse is running and you are in your workbench. 

  2. Select "Install New Software" from the "Help" pull-down menu. 

  3. Select "Mars - http://download.eclipse.org/releases/mars" from the "Work with:" pull-down menu. 

  4. Expand the box next to "Linux Tools" and select "C/C++ Remote (Over TCF/TE) Run/Debug Launcher" and "TM Terminal". 

  5. Expand the box next to "Mobile and Device Development" and select the following boxes: 
    
    
         C/C++ Remote (Over TCF/TE) Run/Debug Launcher
         Remote System Explorer User Actions
         TM Terminal
         TCF Remote System Explorer add-in
         TCF Target Explorer
                            

  6. Expand the box next to "Programming Languages" and select the following boxes: 
    
    
         C/C++ Autotools Support
         C/C++ Development Tools SDK
                            

  7. Complete the installation by clicking through appropriate "Next" and "Finish" buttons. 

### D.1.3. Installing or Accessing the Mars Eclipse Yocto Plug-in¶

You can install the Eclipse Yocto Plug-in into the Eclipse IDE one of two
ways: use the Yocto Project's Eclipse Update site to install the pre-built
plug-in or build and install the plug-in from the latest source code.

#### D.1.3.1. Installing the Pre-built Plug-in from the Yocto Project Eclipse
Update Site¶

To install the Mars Eclipse Yocto Plug-in from the update site, follow these
steps:

  1. Start up the Eclipse IDE. 

  2. In Eclipse, select "Install New Software" from the "Help" menu. 

  3. Click "Add..." in the "Work with:" area. 

  4. Enter `http://downloads.yoctoproject.org/releases/eclipse-plugin/2.2/mars` in the URL field and provide a meaningful name in the "Name" field. 

  5. Click "OK" to have the entry added to the "Work with:" drop-down list. 

  6. Select the entry for the plug-in from the "Work with:" drop-down list. 

  7. Check the boxes next to the following: 
    
    
         Yocto Project SDK Plug-in
         Yocto Project Documentation plug-in
                                

  8. Complete the remaining software installation steps and then restart the Eclipse IDE to finish the installation of the plug-in. 

### Note

You can click "OK" when prompted about installing software that contains
unsigned content.

#### D.1.3.2. Installing the Plug-in Using the Latest Source Code¶

To install the Mars Eclipse Yocto Plug-in from the latest source code, follow
these steps:

  1. Be sure your development system has JDK 1.7+ 

  2. install X11-related packages: 
    
    
         $ sudo apt-get install xauth
                                

  3. In a new terminal shell, create a Git repository with: 
    
    
         $ cd ~
         $ git clone git://git.yoctoproject.org/eclipse-poky
                                

  4. Use Git to checkout the correct tag: 
    
    
         $ cd ~/eclipse-poky
         $ git checkout mars/yocto-2.2
                                

This puts you in a detached HEAD state, which is fine since you are only going
to be building and not developing.

  5. Change to the `scripts` directory within the Git repository: 
    
    
         $ cd scripts
                                

  6. Set up the local build environment by running the setup script: 
    
    
         $ ./setup.sh
                                

When the script finishes execution, it prompts you with instructions on how to
run the `build.sh` script, which is also in the `scripts` directory of the Git
repository created earlier.

  7. Run the `build.sh` script as directed. Be sure to provide the tag name, documentation branch, and a release name.

Following is an example:

    
    
         $ ECLIPSE_HOME=/home/scottrif/eclipse-poky/scripts/eclipse ./build.sh -l mars/yocto-2.2 master yocto-2.2 2>&1 | tee build.log
                                

The previous example command adds the tag you need for `mars/yocto-2.2` to
`HEAD`, then tells the build script to use the local (-l) Git checkout for the
build. After running the script, the file
`org.yocto.sdk-`_`release`_`-`_`date`_`-archive.zip` is in the current
directory.

  8. If necessary, start the Eclipse IDE and be sure you are in the Workbench. 

  9. Select "Install New Software" from the "Help" pull-down menu. 

  10. Click "Add". 

  11. Provide anything you want in the "Name" field. 

  12. Click "Archive" and browse to the ZIP file you built earlier. This ZIP file should not be "unzipped", and must be the `*archive.zip` file created by running the `build.sh` script. 

  13. Click the "OK" button. 

  14. Check the boxes that appear in the installation window to install the following: 
    
    
         Yocto Project SDK Plug-in
         Yocto Project Documentation plug-in
                                

  15. Finish the installation by clicking through the appropriate buttons. You can click "OK" when prompted about installing software that contains unsigned content. 

  16. Restart the Eclipse IDE if necessary. 

At this point you should be able to configure the Eclipse Yocto Plug-in as
described in the "Configuring the Mars Eclipse Yocto Plug-in" section.

### D.1.4. Configuring the Mars Eclipse Yocto Plug-in¶

Configuring the Mars Eclipse Yocto Plug-in involves setting the Cross Compiler
options and the Target options. The configurations you choose become the
default settings for all projects. You do have opportunities to change them
later when you configure the project (see the following section).

To start, you need to do the following from within the Eclipse IDE:

  * Choose "Preferences" from the "Window" menu to display the Preferences Dialog. 

  * Click "Yocto Project SDK" to display the configuration screen. 

The following sub-sections describe how to configure the the plug-in.

### Note

Throughout the descriptions, a start-to-finish example for preparing a QEMU
image for use with Eclipse is referenced as the "wiki" and is linked to the
example on the [ Cookbook guide to Making an Eclipse Debug Capable Image](http
s://wiki.yoctoproject.org/wiki/TipsAndTricks/RunningEclipseAgainstBuiltImage)
wiki page.

#### D.1.4.1. Configuring the Cross-Compiler Options¶

Cross Compiler options enable Eclipse to use your specific cross compiler
toolchain. To configure these options, you must select the type of toolchain,
point to the toolchain, specify the sysroot location, and select the target
architecture.

  * _Selecting the Toolchain Type:_ Choose between `Standalone pre-built toolchain` and `Build system derived toolchain` for Cross Compiler Options. 

    * _ `Standalone Pre-built Toolchain:`_ Select this type when you are using a stand-alone cross-toolchain. For example, suppose you are an application developer and do not need to build a target image. Instead, you just want to use an architecture-specific toolchain on an existing kernel and target root filesystem. In other words, you have downloaded and installed a pre-built toolchain for an existing image. 

    * _ `Build System Derived Toolchain:`_ Select this type if you built the toolchain as part of the [Build Directory](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#build-directory). When you select `Build system derived toolchain`, you are using the toolchain built and bundled inside the Build Directory. For example, suppose you created a suitable image using the steps in the [wiki](https://wiki.yoctoproject.org/wiki/TipsAndTricks/RunningEclipseAgainstBuiltImage). In this situation, you would select the `Build system derived toolchain`. 

  * _Specify the Toolchain Root Location:_ If you are using a stand-alone pre-built toolchain, you should be pointing to where it is installed (e.g. `/opt/poky/2.2`). See the "Installing the SDK" section for information about how the SDK is installed.

If you are using a build system derived toolchain, the path you provide for
the `Toolchain Root Location` field is the [Build
Directory](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html
#build-directory) from which you run the `bitbake` command (e.g
`/home/scottrif/poky/build`).

For more information, see the "Building an SDK Installer" section.

  * _Specify Sysroot Location:_ This location is where the root filesystem for the target hardware resides. 

This location depends on where you separately extracted and installed the
target filesystem. As an example, suppose you prepared an image using the
steps in the [wiki](https://wiki.yoctoproject.org/wiki/TipsAndTricks/RunningEc
lipseAgainstBuiltImage). If so, the `MY_QEMU_ROOTFS` directory is found in the
[Build Directory](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-
manual.html#build-directory) and you would browse to and select that directory
(e.g. `/home/scottrif/build/MY_QEMU_ROOTFS`).

For more information on how to install the toolchain and on how to extract and
install the sysroot filesystem, see the "Building an SDK Installer" section.

  * _Select the Target Architecture:_ The target architecture is the type of hardware you are going to use or emulate. Use the pull-down `Target Architecture` menu to make your selection. The pull-down menu should have the supported architectures. If the architecture you need is not listed in the menu, you will need to build the image. See the "[Building Images](http://www.yoctoproject.org/docs/2.2/yocto-project-qs/yocto-project-qs.html#qs-building-images)" section of the Yocto Project Quick Start for more information. You can also see the [wiki](https://wiki.yoctoproject.org/wiki/TipsAndTricks/RunningEclipseAgainstBuiltImage). 

#### D.1.4.2. Configuring the Target Options¶

You can choose to emulate hardware using the QEMU emulator, or you can choose
to run your image on actual hardware.

  * _QEMU:_ Select this option if you will be using the QEMU emulator. If you are using the emulator, you also need to locate the kernel and specify any custom options.

If you selected the `Build system derived toolchain`, the target kernel you
built will be located in the [Build
Directory](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html
#build-directory) in `tmp/deploy/images/_`machine`_` directory. As an example,
suppose you performed the steps in the [wiki](https://wiki.yoctoproject.org/wi
ki/TipsAndTricks/RunningEclipseAgainstBuiltImage). In this case, you specify
your Build Directory path followed by the image (e.g.
`/home/scottrif/poky/build/tmp/deploy/images/qemux86/bzImage-qemux86.bin`).

If you selected the standalone pre-built toolchain, the pre-built image you
downloaded is located in the directory you specified when you downloaded the
image.

Most custom options are for advanced QEMU users to further customize their
QEMU instance. These options are specified between paired angled brackets.
Some options must be specified outside the brackets. In particular, the
options `serial`, `nographic`, and `kvm` must all be outside the brackets. Use
the `man qemu` command to get help on all the options and their use. The
following is an example:

    
    
        serial ‘<-m 256 -full-screen>’
                                

Regardless of the mode, Sysroot is already defined as part of the Cross-
Compiler Options configuration in the `Sysroot Location:` field.

  * _External HW:_ Select this option if you will be using actual hardware.

Click the "Apply" and "OK" to save your plug-in configurations.

## D.2. Creating the Project¶

You can create two types of projects: Autotools-based, or Makefile-based. This
section describes how to create Autotools-based projects from within the
Eclipse IDE. For information on creating Makefile-based projects in a terminal
window, see the "Makefile-Based Projects" section.

### Note

Do not use special characters in project names (e.g. spaces, underscores,
etc.). Doing so can cause configuration to fail.

To create a project based on a Yocto template and then display the source
code, follow these steps:

  1. Select "C Project" from the "File -> New" menu. 

  2. Expand `Yocto Project SDK Autotools Project`. 

  3. Select `Hello World ANSI C Autotools Projects`. This is an Autotools-based project based on a Yocto template. 

  4. Put a name in the `Project name:` field. Do not use hyphens as part of the name (e.g. `hello`). 

  5. Click "Next". 

  6. Add appropriate information in the various fields. 

  7. Click "Finish". 

  8. If the "open perspective" prompt appears, click "Yes" so that you in the C/C++ perspective. 

  9. The left-hand navigation pane shows your project. You can display your source by double clicking the project's source file. 

## D.3. Configuring the Cross-Toolchains¶

The earlier section, "Configuring the Mars Eclipse Yocto Plug-in", sets up the
default project configurations. You can override these settings for a given
project by following these steps:

  1. Select "Yocto Project Settings" from the "Project -> Properties" menu. This selection brings up the Yocto Project Settings Dialog and allows you to make changes specific to an individual project.

By default, the Cross Compiler Options and Target Options for a project are
inherited from settings you provided using the Preferences Dialog as described
earlier in the "Configuring the Mars Eclipse Yocto Plug-in" section. The Yocto
Project Settings Dialog allows you to override those default settings for a
given project.

  2. Make or verify your configurations for the project and click "OK". 

  3. Right-click in the navigation pane and select "Reconfigure Project" from the pop-up menu. This selection reconfigures the project by running `autogen.sh` in the workspace for your project. The script also runs `libtoolize`, `aclocal`, `autoconf`, `autoheader`, `automake --a`, and `./configure`. Click on the "Console" tab beneath your source code to see the results of reconfiguring your project. 

## D.4. Building the Project¶

To build the project select "Build All" from the "Project" menu. The console
should update and you can note the cross-compiler you are using.

### Note

When building "Yocto Project SDK Autotools" projects, the Eclipse IDE might
display error messages for Functions/Symbols/Types that cannot be "resolved",
even when the related include file is listed at the project navigator and when
the project is able to build. For these cases only, it is recommended to add a
new linked folder to the appropriate sysroot. Use these steps to add the
linked folder:

  1. Select the project. 

  2. Select "Folder" from the `File > New` menu. 

  3. In the "New Folder" Dialog, select "Link to alternate location (linked folder)". 

  4. Click "Browse" to navigate to the include folder inside the same sysroot location selected in the Yocto Project configuration preferences. 

  5. Click "OK". 

  6. Click "Finish" to save the linked folder. 

## D.5. Starting QEMU in User-Space NFS Mode¶

To start the QEMU emulator from within Eclipse, follow these steps:

### Note

See the "[Using the Quick EMUlator
(QEMU)](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#dev-
manual-qemu)" chapter in the Yocto Project Development Manual for more
information on using QEMU.

  1. Expose and select "External Tools Configurations ..." from the "Run -> External Tools" menu. 

  2. Locate and select your image in the navigation panel to the left (e.g. `qemu_i586-poky-linux`). 

  3. Click "Run" to launch QEMU. 

### Note

The host on which you are running QEMU must have the `rpcbind` utility running
to be able to make RPC calls on a server on that machine. If QEMU does not
invoke and you receive error messages involving `rpcbind`, follow the
suggestions to get the service running. As an example, on a new Ubuntu 16.04
LTS installation, you must do the following in order to get QEMU to launch:

    
    
         $ sudo apt-get install rpcbind
                            

After installing `rpcbind`, you need to edit the `/etc/init.d/rpcbind` file to
include the following line:

    
    
         OPTIONS="-i -w"
                            

After modifying the file, you need to start the service:

    
    
         $ sudo service portmap restart
                            

  4. If needed, enter your host root password in the shell window at the prompt. This sets up a `Tap 0` connection needed for running in user-space NFS mode. 

  5. Wait for QEMU to launch. 

  6. Once QEMU launches, you can begin operating within that environment. One useful task at this point would be to determine the IP Address for the user-space NFS by using the `ifconfig` command. The IP address of the QEMU machine appears in the xterm window. You can use this address to help you see which particular IP address the instance of QEMU is using. 

## D.6. Deploying and Debugging the Application¶

Once the QEMU emulator is running the image, you can deploy your application
using the Eclipse IDE and then use the emulator to perform debugging. Follow
these steps to deploy the application.

### Note

Currently, Eclipse does not support SSH port forwarding. Consequently, if you
need to run or debug a remote application using the host display, you must
create a tunneling connection from outside Eclipse and keep that connection
alive during your work. For example, in a new terminal, run the following:

    
    
         $ ssh -XY _user_name_@_remote_host_ip_
                    

Using the above form, here is an example:

    
    
         $ ssh -XY root@192.168.7.2
                    

After running the command, add the command to be executed in Eclipse's run
configuration before the application as follows:

    
    
         export DISPLAY=:10.0
                    

Be sure to not destroy the connection during your QEMU session (i.e. do not
exit out of or close that shell).

  1. Select "Debug Configurations..." from the "Run" menu.

  2. In the left area, expand `C/C++Remote Application`. 

  3. Locate your project and select it to bring up a new tabbed view in the Debug Configurations Dialog. 

  4. Click on the "Debugger" tab to see the cross-tool debugger you are using. Be sure to change to the debugger perspective in Eclipse. 

  5. Click on the "Main" tab. 

  6. Create a new connection to the QEMU instance by clicking on "new".

  7. Select `SSH`, which means Secure Socket Shell. Optionally, you can select an TCF connection instead. 

  8. Click "Next". 

  9. Clear out the "Connection name" field and enter any name you want for the connection. 

  10. Put the IP address for the connection in the "Host" field. For QEMU, the default is `192.168.7.2`. However, if a previous QEMU session did not exit cleanly, the IP address increments (e.g. `192.168.7.3`). 

### Note

You can find the IP address for the current QEMU session by looking in the
xterm that opens when you launch QEMU.

  11. Enter `root`, which is the default for QEMU, for the "User" field. Be sure to leave the password field empty. 

  12. Click "Finish" to close the New Connections Dialog. 

  13. If necessary, use the drop-down menu now in the "Connection" field and pick the IP Address you entered. 

  14. Assuming you are connecting as the root user, which is the default for QEMU x86-64 SDK images provided by the Yocto Project, in the "Remote Absolute File Path for C/C++ Application" field, browse to `/home/root`. You could also browse to any other path you have write access to on the target such as `/usr/bin`. This location is where your application will be located on the QEMU system. If you fail to browse to and specify an appropriate location, QEMU will not understand what to remotely launch. Eclipse is helpful in that it auto fills your application name for you assuming you browsed to a directory. 

### Note

If you are prompted to provide a username and to optionally set a password, be
sure you provide "root" as the username and you leave the password field
blank.

  15. Be sure you change to the "Debug" perspective in Eclipse. 

  16. Click "Debug" 

  17. Accept the debug perspective. 

## D.7. Using Linuxtools¶

As mentioned earlier in the manual, performance tools exist (Linuxtools) that
enhance your development experience. These tools are aids in developing and
debugging applications and images. You can run these tools from within the
Eclipse IDE through the "Linuxtools" menu.

For information on how to configure and use these tools, see
[http://www.eclipse.org/linuxtools/](http://www.eclipse.org/linuxtools/).

