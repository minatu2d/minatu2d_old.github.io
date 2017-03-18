Ghi chú![](figures/yocto-project-transp.png)

## Giới thiệu nhanh về Yocto Project

Copyright © 2010-2016 Linux Foundation

Permission is granted to copy, distribute and/or modify this document under
the terms of the [Creative Commons Attribution-Share Alike 2.0 UK: England &
Wales](http://creativecommons.org/licenses/by-sa/2.0/uk/) as published by
Creative Commons.

### Ghi chú

Phiên bản mới nhất của tài liệu này sẽ được cập nhật mỗi khi Yocto Project release, xem thêm tại  [Yocto Project Quick Start](http://www.yoctoproject.org/docs/2.2/yocto-project-qs/yocto-project-qs.html) từ website của dự án.

* * *

## Lời chào!

Chào mừng đến với Yocto Project! The Yocto Project là dự án mã nguồn mở, cộng tác, hướng đến các developers của hệ thống Linux nhúng.
Trong đó, Yocto Project chọn thống build là kết quả của dự án OpenEmbedded (OE), nó sử dụng công cụ [BitBake](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#bitbake-term), để tạo nên một hệ thống Linux hoàn chỉnh.
Các thành phần của BitBake and OE được kết hợp với nhau trong một hệ thống build, được gọi là [Poky](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#poky).

Nếu bạn chưa chạy Linux trên máy của bạn, hãy thử chạy Yocto Project trên đó xem, bạn có thể xem xét phần Yocto Project Build Appliance nếu bạn muốn thử. Build Appliance cho phép bạn build và boot một bản Linux được tùy biến 
sử dụng Yocto Project trên một hệ thống không sử dụng Linux. xem thêm ở [Yocto Project Build Appliance](https://www.yoctoproject.org/tools-resources/projects/build-appliance).

Tài liệu này giới thiệu nhanh này mong muốn giúp bạn có thể nhanh chóng setup được một môi trường build cho Yocto Project và build một vài bản Linux của riêng bạn.
Không đi vào tìm hiểu chi tiết hơn về Yocto Project và những khả năng của nó, tài liệu này cung cấp những thông tin tối giản nhất cần cần thiết để thử ngay với Yocto Project sử dụng môi trường build Linux. Sau khi đọc và làm theo các hướng dẫn trong tài liệu, bạn sẽ hiểu được Yocto Project là gì và làm thế nào để sử dụng các thành phần của nó.
Bạn cũng sẽ được hướng dẫn từng bước để tạo ra 2 ảnh hệ thống: 1 cái dành cho phần cứng mô phỏng, một cái dành cho phần cứng thật.
Các ví dụ đều sẽ chỉ cho bạn thấy sự dễ dàng khi sử dụng Yocto Project để tạo nhiều loại ảnh hệ thống cho nhiều loại phần cứng khác nhau.

Thông tin chi tiết về Yocto Project, bạn có thể tham khảo các nguồn sau:

  * _Website:_ Dự án Yocto hay [Yocto Project Website](http://www.yoctoproject.org) cung cấp các phiên bản mới nhất của Yocto Project, tin tức, toàn bộ tài liệu, cũng như đường dẫn đến một cộng đông Yocto Project Development Community rất sôi nổi.

  * _FAQs:_ Danh sách các câu hỏi phổ biến về Yocto Project cùng câu trả lời. Bạn có thể tìm FAQs ở: [Yocto Project FAQ](https://wiki.yoctoproject.org/wiki/FAQ) dạng một trang wiki, và chương "[FAQ](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#faq)" trong tài liệu tham khảo Yocto Project.

  * _Developer Screencast:_[Getting Started with the Yocto Project - New Developer Screencast Tutorial](http://vimeo.com/36450321) cung cấp các đoạn video khoảng 30-minute video cho người sử dụng chưa quen với Yocto Project dù đã từng sử dụng Linux. Những screencast này có thể đã cũ, tuy nhiên phần hướng dẫn cùng với các khái niệm nền tảng sẽ rất có ích với người mới.

## Giới thiệu môi trường phát triển của Yocto Project

Yocto Project thông qua hệ thống build OpenEmbedded(OE) để cung cấp môi trường phát triển mã nguồn mở cho các ứng dụng trên các kiến trúc ARM, MIPS, PowerPC, and x86; nó có thể chạy trên rất nhiều platform khác nhau bao gồm cả x86_64 và các môi trường giả lập của nó.
Bạn có thể sử dụng các thành phần từ Yocto Project để design, develop, build, debug, simulate (giả lập phần cứng), and test toàn bộ phần mềm từ hệ thống đến ứng dụng (software stack) trên Linux, bao gồm X Window System (hệ thống quản lý của sổ, giao diện), GTK+ frameworks (tạo giao diện), and Qt frameworks (cho phát triển giao diện và các ứng dụng liên quan).

![](figures/yocto-environment.png)

Môi trường phát triển Yocto Project

Dưới đây là một vài đặc điểm chính của môi trường phát triển Yocto Project:

  * Cung cấp một nhân Linux kernel khá mới kèm theo các lệnh hệ thống và thư viện cho phát triển hệ thống nhúng.

  * Cho phép các thành phần X11, GTK+, Qt, Clutter, and SDL (và nhiều thứ tương tự) được đưa vào sử dụng dễ dàng, vì thế bạn có thể tạo một giao diện tương tác "đẹp", "ngon lành cành đào" trên màn hình hiển thị (nếu có). Còn với các hệ thống không có màn hình hiển thị, thì bạn không cần cài đặt gì nữa vì chúng luôn có sẵn rồi (console).

  * Có phần core ổn định tương thích với dự án OpenEmbedded vì thế bạn có thể tin tưởng được và dễ dàng sử dụng.

  * Support đầy đủ một loạt phần cứng và thiết bị mô phỏng thông qua Quick Emulator(QEMU - Một chương trình mô phỏng cực kì phổ biến).

  * Cung cấp 1 cơ chế phân lớp cho phép bạn dễ dàng mở rộng hệ thống, thực hiện thay đổi, và quản lý một cách có tổ chức.

Bạn có thể sử dụng Yocto Project để sinh ảnh hệ thống cho nhiều loại thiết bị. Như đã nói ở phần đầu, Yocto Project hỗ trợ việc tạo các ảnh tham chiếu của hệ thống, vì thế bạn có thể build và mô phỏng hoạt động của ứng dụng sử dụng QEMU (mà không cần đến phần cứng thật).
Các máy mà QEMU có thể mô phỏng đầy đủ gồm cả 32-bit và 64-bit trên các kiến trúc x86, ARM, MIPS, and PowerPC. Hiểu khả năng mô phỏng này, bạn có thể sử dụng cơ chế lớp để mở rộng việc chạy ứng dụng trên nhiều platform cái mà ta biết Linux có thể chạy và ta có toolchain cho nó.

Một tính năng khác của Yocto Project, đó là giao diện người dùng tham chiếu Sato. Đây là UI không được đưa mặc định vào ảnh hệ thống, nó dựa trên GTK+, hướng đến các thiết bị có kích thước màn hình hạn chế, nó cũng là một phần của OpenEmbedded Core layer vì thế developers có thể test các thành phần của phần mềm dựa trên giao diện này.

## Thiết lập môi trường sử dụng Yocto Project

Danh sách dưới đây chỉ ra những thứ cần thiết để sử dụng môi trường build chạy Linux
cho việc build ảnh hệ thống bằng Yocto Project:

  * _Build Host_ Môi trường build nên có ít nhất 50GB đĩa trống chạy một trong các bản phân phối Linux sau: Các phiên bản gần đây của Fedora, openSUSE, CentOS, Debian, hoặc Ubuntu).

  * _Build Host Packages_ Các gói tương ứng cần được cài trên môi trường build.

  * _The Yocto Project_ Một phiên bản của Yocto Project.

### Về bản phân phối Linux

Team Yocto Project thường chạy thử trên các phiên bản ổn định gần đây của các distro Linux phổ biến. Về cơ bản, nếu bạn có từ phiên bản ngay trước phiên bản ổn định mới nhất của các distro dưới đây, thì thường sẽ không có vấn đề gì khi chạy Yocto Project.

  * Ubuntu

  * Fedora

  * openSUSE

  * CentOS

  * Debian

Danh sách chi tiết của các distro hỗ trợ Yocto Project có thể xem tại chương "[Supported Linux Distributions](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#detailed-supported-distros)" trong Yocto Project Reference Manual.

Hệ thống build OpenEmbedded có thể chạy trên bất cứ hệ thống nào chứa
các phiên bản phù hợp của các phần mềm Git, tar, and Python.

  * Git 1.8.3.1 or greater

  * tar 1.24 or greater

  * Python 3.4.0 or greater.

Nếu hệ thống của bạn không thỏa mãn bất cứ điều kiện nào ở trên, bạn có thể thực hiện một vài bước để chuẩn bị cho nó. Xem tại chương "[Required Git, tar, and Python
Versions](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#required-git-tar-and-python-versions)" trong hướng dẫn tham khảo Yocto Project.

### Các gói cho hệ thống build

Yêu cầu các gói cần có cho host (máy chạy Yocto Project) phụ thuộc vào mục đích sử dụng Yocto Project của bạn. Ví dụ, nếu bạn muốn build một "image" mà chạy được trên QEMU ở chế độ đồ họa (graphical mode) ( nó có thể dựa trên một ảnh tối thiểu (minimal), hoặc cơ bản (basic) này), nói chung yêu cầu về các gói cần thiết cho host cũng khác nhau khi build một "image" nhỏ gọn hoặc build một "image" nằm ngoài danh sách image được liệt kê trong Yocto Project.

Tổng hợp lại, số lượng gói yêu cầu phải cài sẽ lớn nếu bạn muốn phủ (cover) hết các trường hợp sử dụng.

### Ghi chú

Nói chung, bạn cần quyền root để tiến hành cài đặt các gói. Vì thế, các command bên dưới đây có thể có hoặc không chạy phụ thuộc vào hệ thống (distribition - bản phân phố) của bạn có cài đặt "sudo" hay không.

Những package được chỉ ra dưới đây cần được cài đặt để có thể hỗ trợ chế độ đồ họa (ví dụ: chế độ cơ bản + hỗ trợ đồ họa). Danh sách các gói cho các ngữ cảnh khác xin hãy xem thêm tại chương "[Required Packages
for the Host Development System](http://www.yoctoproject.org/docs/2.2/ref-
manual/ref-manual.html#required-packages-for-the-host-development-system)"
 trong hướng dẫn tham khảo của Yocto Project.

  * _Ubuntu and Debian_
         $ sudo apt-get install gawk wget git-core diffstat unzip texinfo gcc-multilib \
         build-essential chrpath socat libsdl1.2-dev xterm

  * _Fedora_
         $ sudo dnf install gawk make wget tar bzip2 gzip python3 unzip perl patch \
         diffutils diffstat git cpp gcc gcc-c++ glibc-devel texinfo chrpath \
         ccache perl-Data-Dumper perl-Text-ParseWords perl-Thread-Queue perl-bignum socat \
         findutils which SDL-devel xterm

  * _OpenSUSE_
         $ sudo zypper install python gcc gcc-c++ git chrpath make wget python-xml \
         diffstat makeinfo python-curses patch socat libSDL-devel xterm

  * _CentOS_

         $ sudo yum install gawk make wget tar bzip2 gzip python unzip perl patch \
         diffutils diffstat git cpp gcc gcc-c++ glibc-devel texinfo chrpath socat \
         perl-Data-Dumper perl-Text-ParseWords perl-Thread-Queue SDL-devel xterm

### Ghi chú

Người sử dụng CentOS 6.x cần đảm bảo phiên bản được yêu cầu của Git, tar và Python. Chi tiết xin hãy xem tại chương "[Required Git, tar, and PythonVersions](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#required-git-tar-and-python-versions)" trong hướng dẫn tham khảo của Yocto Project.

### Các phiên bản của Yocto Project

Điều cuối cùng các bạn cần chắc chắn trước khi sử dụng Yocto Project phiên bản của chính Yocto Project. Có khuyến cáo rằng nên lấy phiên bản mới nhất bằng cách sử dụng thiết lập (tức là cloning trong [Git](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#git)) một bản copy kho chứa Git (Git repository) của `poky` trên máy host sau đó checkout (cập nhật) phiên bản mới nhất. Điều này cho phép bạn dễ dàng cập nhật phiên bản mới hơn của Yocto Project cũng như đóng góp trở lại (contribute back) cho Yocto Project.

Dưới đây là một ví dụ trên máy Ubuntu, nó at clones kho chứa `poky` và checkout theo phiên bản mới nhất của Yocto Project (i.e. 2.2):



         $ git clone git://git.yoctoproject.org/poky
         Cloning into 'poky'...
         remote: Counting objects: 226790, done.
         remote: Compressing objects: 100% (57465/57465), done.
         remote: Total 226790 (delta 165212), reused 225887 (delta 164327)
         Receiving objects: 100% (226790/226790), 100.98 MiB | 263 KiB/s, done.
         Resolving deltas: 100% (165212/165212), done.
         $ git checkout morty


Bạn có có thể có được các phiên bản của Yocto bằng tải trực tiếp từ trang chủ của [Yocto Project website](http://www.yoctoproject.org).

Các thông tin thêm về việc thiết lập theo từng phiên bản của Yocto Project đều có đầy đủ tại "[Yocto Project Release](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#local-yp-release)"  trong hướng dẫn tham khảo dành cho phát triển của Yocto Project.

## Tạo một ảnh hệ thống

Giờ sau khi bạn đã có một môi trường đáp ứng đầy đủ các yêu cầu cần thiết, bạn có thể bắt đầu Yocto Project. Bạn có thể thao tác với Yocto bằng giao diện dòng lệnh (command-line) hoặc sử dụng một giao diện đồ họa được gọi là Toaster. Nếu bạn muốn sử dụng Toaster có thể xem thêm ở [Toaster User Manual](http://www.yoctoproject.org/docs/2.2/toaster-manual/toaster-
manual.html) để biết thông tin chi tiết về cách cài đặt cũng như cấu hình cho Toaster.

Còn với giao diện dòng lệnh, bạn có thể tiếp tục với hướng dẫn này với từng bước cho đến kết quả cuối cùng:

  * Tạo một ảnh hệ thống tham chiếu `qemux86` và chạy nó trên giả lập máy tính QEMU.

  * Dễ dàng thay đổi cấu hình vì thế bạn dễ dàng tạo một "ảnh" khác, rồi ghi nó lên một thiết bị lưu trữ có khả năng khởi động (bootable media) và xem kết quả trên phần cứng thật. Ví dụ này sử dụng phần cứng tương thích với board MinnowBoard MAX.

### Ghi chú

Các bước trong 2 chương tiếp theo không đưa ra chi tiết, mà chỉ đưa dạng ngắn gọn nhất, các câu lệnh được đưa ra để phù hợp cho việc tiếp cận thôi. Về chi tiết mỗi câu lệnh, các bạn có thể xem thêm trong tập tài liệu [Yocto Project
manual set](http://www.yoctoproject.org/documentation).

### Tạo một ảnh cho máy giả lập Emulation

Sử dụng các câu lệnh dưới đây để build một ảnh hệ thống. Hệ thống build OpenEmbedded sẽ tạo toàn bộ một bản phân phối Linux (Linux distribution) bao gồm cả toolchain hoàn toàn từ source code (mã nguồn).

### Ghi chú về Network Proxies

Ban đầu, quá trình build sẽ tìm source ở trên một tập các địa chỉ có sẵn. Nếu bạn đang sử dụng tường lửa ở máy host và không set proxy cho nó, thì bạn có thể gặp vấn đề trong quá trình build khi hệ thống Build cố gắng tải source về ( ví dụ ví dị việc tải bị failure hoặc Git bị failure).

Nếu bạn gặp vấn đề mà không biết cách thiết lập proxy, hãy tìm hiểu về nó. Một nơi thường thấy nhất là từ Thiết lập của Web Browser. Cuối cùng bạn có thể tìm thêm thông tin phần các câu hỏi thường gặp (FAQ) trong hướng dẫn tham khảo Yocto Project [FAQ](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#how-does-the-yocto-project-obtain-source-code-and-will-it-work-behind-my-firewall-or-proxy-server) và trong "[Working Behind a NetworkProxy](https://wiki.yoctoproject.org/wiki/Working_Behind_a_Network_Proxy)" nữa.

  1. _Hãy chắc chắn là máy host của bạn đã được setup:_ Các bước tiếp theo sử dụng để tạo Image trong chương này phụ thuộc vào môi trường đã được setup chuẩn hay chưa đấy. Vì thế, hãy chắc chắn rằng bạn đã ngó qua phần mô tả trong chương "Setting Up to Use the Yocto Project" rồi.

  2. _Checkout phiên bản:_ Chắc chắn rằng bạn đang ở trong thư mục source [Source Directory](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#source-directory) (ví dụ: `poky` chẳng hạn) và kiểm tra phiên bản mới nhất của Yocto:


         $ cd ~/poky
         $ git checkout -b morty origin/morty


Lệnh `checkout` của Git sẽ lấy phiên bản được chỉ định xuống local thông qua tên branch (ví dụ `morty` chẳng hạn). Phiên bản được lấy xuống chính là branch chỉ định tại thời điểm đó. Tức là chúng ta sẽ có các file mới nhất của branch đó.

  3. _Khởi tạo môi trường Build:_ Hãy chạy script thiết lập môi trường [`oe-init-build-env`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#structure-core-script) để định nghĩa các biến cần thiết cho hệ thống build OpenEmbedded máy build của bạn bằng câu lệnh sau.


         $ source oe-init-build-env


Ở câu lệnh trên, Script sẽ tự động tạo [Build Directory](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#build-directory), và trong trường hợp này thư mục `build` nằm bên dưới [Source
Directory](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#source-directory). Sau khi chạy script thì, thư mục làm việc hiện tại cũng được chuyển vào thư mục Build luôn. Kể từ giờ, đến lúc hoàn thành mọi thứ, thư mục Build chứa tất cả các file được tạo trong quá trình build.

### Ghi chú
Để có thêm thông tin về việc BitBake thường chú trên bộ nhớ (memory-resident) [BitBake](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#usingpoky-components-bitbake), hãy xem chi tiết về Script [`oe-init-build-env-memres`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#structure-memres-core-script).


  4. _Xem xét các file cấu hình nội bộ (Local Configuration File):_ Sau khi chạy xong script setup môi trường, bạn sẽ thấy 1 file có tên là `local.conf` trong thư mục`conf` nằm bên dưới thư mục Build. Trước khi sử dụng BitBake để bắt đầu build, bạn có thể xem nội dung file và chắc chắn những thứ bạn muốn:

    * Để giúp tiết kiệm dung lượng ổ cứng trong quá trình build, bạn có thể thêm dòng sau đây vào file cấu hình nội bộ trong project của bạn, trong ví dụ ở trên file đó là  `poky/build/conf/local.conf`. Thêm dòng này, thư mục working khi thực hiện build một recipe sẽ bị xóa.


         INHERIT += "rm_work"


  	* Mặc định, máy target machine cho lần build này là `qemux86`, có nghĩa là ảnh được tạo ra sẽ chạy trên QEMU emulator với kiến trúc CPU họ Intel® 32-bit . Bạn có thể thay đổi nó dễ dàng thông qua biến [`MACHINE`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-MACHINE) vì thế bạn dễ dàng tạo một ảnh cho kiến trúc hoặc platform mới.

    * Một điểm khác cần xem xét trước khi build là chương trình quản lý gói phần mềm nào (package manager) sẽ được sử dụng khi tạo image. Mặc định RPM được chọn trong file `local.conf` là chương trình quản lý gói phần mềm khi tạo Image. Bạn có thể điều chỉnh thông tố này sử dụng biến`[`PACKAGE_CLASSES`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-PACKAGE_CLASSES)`.

Việc lựa chọn trình quán lý gói phần mềm (package manager) ở đây không liên quan đến việc có sử dụng hay không sử dụng công cụ quản lý gói khi Image được chạy trên Target.

Thông tin về các lựa chọn cho trình quản lý gói (package manager selection) có thể thấy ở chương "[`package.bbclass`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#ref-classes-package)" trong hướng dẫn tham khảo Yocto Project.

  5. _Bắt đầu Build:_ Tiếp tục với câu lệnh dưới đây để tạo ra một ảnh hệ điều hành cho target của bạn, ở đây ảnh có tên `core-image-sato` được chọn: 

### Ghi chú

Phụ thuộc vào số processor, số cores, dung lượng RAM, tốc độ đường truyền Internet và các yếu tố khác, quá trình build có thể mất đến vài giờ cho lần build đầu tiên. Còn đối với những lần build sau đó, sẽ nhanh hơn rất nhiều vì nhiều thứ được cached lại rồi.



         $ bitbake core-image-sato


Thông tin chi tiết về cách sử dụng câu lệnh `bitbake` có thể xem tại chương "[BitBake](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#usingpoky-components-bitbake)" trong hướng dẫn tham khảo Yocto Project, hoặc xem ở chương "[BitBake Command](http://www.yoctoproject.org/docs/2.2/bitbake-
user-manual/bitbake-user-manual.html#bitbake-user-manual-command)" trong hướng dẫn sử dụng BitBake cho người dùng. Thông tin về các các ảnh hệ thống có thể chọn khác, có thể xem thêm tại chương "[Images](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#ref-images)" trong hướng dẫn tham khảo Yocto Project.

  6. _Chạy thử ảnh hệ thống bằng QEMU:_ Khi đã có ảnh hệ thống rồi, bạn có thể khởi động QEMU và chạy hệ hệ thống trong ảnh đó:


         $ runqemu qemux86


Nếu bạn muốn tìm hiểu thêm về QEMU, có thể xem thêm tại chương "[Using the Quick EMUlator (QEMU)](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#dev-manual-qemu)" trong hướng dẫn phát triển Yocto Project.

  7. _Thoát QEMU:_ Để thoát QEMU, đơn giản bạn đóng cửa sổ hoăc mở 1 terminal và chạy lệnh `poweroff`.

### Build ảnh cho phần cứng thật

Các câu lệnh dưới đây sẽ chỉ và việc tạo ảnh cho một máy mới dễ dàng ra sao. Những step này thực hiện cho phần cứng MinnowBoard MAX, cái mà được supported bởi Yocto Project và các gói hỗ trợ Board (BSP) `meta-intel` `intel-corei7-64` và `intel-core2-32`.

### Ghi chú

Board mạch MinnowBoard MAX được cài đặt mặc định là firmware 64-bit. Nếu bạn muốn sử dụng mode 32-bit, bạn phải cài đặt firmware [32-bit](http://firmware.intel.com/projects/minnowboard-max).

  1. _Lấy 1 bản copy của `meta-intel`:_ Để tạo image cho MinnowBoard MAX cần phải có layer `meta-intel`. Có thể sử dụng câu lệnh `git clone` để lấy 1 bản copy vào [Source Directory](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#source-directory), Trong ví dụ ở trên thư mục đó là `poky`:


         $ cd $HOME/poky
         $ git clone git://git.yoctoproject.org/meta-intel
         Cloning into 'meta-intel'...
         remote: Counting objects: 11988, done.
         remote: Compressing objects: 100% (3884/3884), done.
         Receiving objects: 100% (11988/11988), 2.93 MiB | 2.51 MiB/s, done.
         remote: Total 11988 (delta 6881), reused 11752 (delta 6645)
         Resolving deltas: 100% (6881/6881), done.
         Checking connectivity... done.


Về cơ bản, khi clone một Git repository, nhánh "master" sẽ được tải về. Trước khi bạn build image sử dụng layer `meta-intel`,  thì bạn phải chắc chắn rằng 2 cái đó (`meta-intel` và `poky`) đang sử dụng cùng 1 phiên bản. Trong trường hợp này, bạn cần checkout nhánh "`morty`" của layer `meta-intel` sau khi clone:



         $ cd $HOME/poky/meta-intel
         $ git checkout morty
         Branch morty set up to track remote branch morty from origin.
         Switched to a new branch 'morty'


  2. _Cấu hình trước khi Build:_ Để cấu hình cho việc build, bạn có thể edit các file `bblayers.conf` và `local.conf`, cả 2 file này đều nằm dưới thư mục `build/conf`.

Dưới đây là 1 cách nhanh chóng để edit 2 file này. Câu lệnh đầu tiên sử dụng là `bitbake-layers add-layer` tức là để thêm layer `meta-intel`, layer chứa các BSP của `intel-core*`. Câu lệnh thứ 2 sử dụng để chọn BSP bằng cách thiết lập biến [`MACHINE`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-MACHINE).



         $ cd $HOME/poky/build
         $ bitbake-layers add-layer "$HOME/poky/meta-intel"
         $ echo 'MACHINE = "intel-corei7-64"' >> conf/local.conf


### Ghi chú

Nếu muốn một bản build 64-bit, thì sử dụng câu lệnh sau:



         $ echo 'MACHINE = "intel-corei7-64"' >> conf/local.conf


Còn nếu muốn một bản build 32-bit, thì sử dụng những câu lệnh sau:



         $ echo 'MACHINE = "intel-core2-32"' >> conf/local.conf


  3. _Tạo Image cho board MinnowBoard MAX:_ Loại Image mà bạn build phụ thuộc vào mục đích sử dụng. Ví dụ, ở ví dụ trước chúng ta tạo Image tên là `core-image-sato`, cái mà hỗ trợ giao diện Sato. Bạn có thể build rất nhiều loại Image cho MinnowBoard MAX. Nó có thể là `core-image-base`, cái chỉ có giảo diện console. Một lựa chọn khác đầy đủ hơn là `core-image-full-cmdline`, cũng chỉ có giao diện console nhưng có thêm những tính năng của một hệ thống Linux đầy đủ (full-features Linux system). Về các loại image khác mà bạn có thể build khi sử dụng Yocto Project, có thể xem thêm tại chương "[Images](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#ref-images)" trong hướng dẫn tham khảo Yocto Project.

Bởi vì cấu hình được thay đổi ít nhất khi buid lần 2 trở đi, hệ thống build OpenEmbedded có thể sử dụng lại các file từ bản build trước đó nhiều nhất có thể. Việc sử dụng lại này đồng nghĩa với từ lần build thứ 2 trở đi, tốc độ sẽ nhanh hơn rất nhiều so với lần build đầu tiên. Ví dụ, Image `core-image-base` được build bằng câu lệnh:



         $ bitbake core-image-base


Khi quá trình build kết thúc, một ảnh chỉ có giao diện console sẽ được tạo ra ở đường dẫn dưới đây trong thư mục Build (Build Directory):



         tmp/deploy/images/intel-corei7-64/core-image-base-intel-corei7-64.wic


  4. _Ghi Image ra thiết bị lưu trữ:_ Bạn có thể ghi image ra thiết bị có khả năng build như (ví dụ: a USB key, SATA drive, SD card, vân vân.) sử dụng tiện ích `dd`:


         $ sudo dd if=tmp/deploy/images/intel-corei7-64/core-image-base-intel-corei7-64.wic of=TARGET_DEVICE


Ở câu lệnh trên, `TARGET_DEVICE` là một device node trên máy host ( ví dụ: `/dev/sdc` nếu là USB Stick, hoặc `/dev/mmcblk0` nếu là một SD card).

  5. _Boot vào Hardware:_ Với thiết bị boot đã được chuẩn bị ở trên, bạn có thể cắm vào board MinnowBoard MAX sau đó boot hệ thống. Board thường sẽ tự động phát hiện thiết bị lưu trữ và chạy vào bootloader tiếp theo đó là hệ điều hành.

Nếu Board không tự động boot, bạn có thể boot bằng tay theo các câu lệnh dưới đây được thực hiện trên trên EFI shell:



         Shell> connect -r
         Shell> map -r
         Shell> fs0:
         Shell> bootx64


### Ghi chú

Với Image 32-bit thì câu lệnh sẽ như sau:



         Shell> bootia32


## Bước tiếp theo

Nếu bạn có thể hoàn thành tất cả các bước trong chương trước thì xin chúc mừng!　Nào, thế bây giờ làm gì tiếp đây?

Phụ thuộc vào cái bạn định làm trước khi tiếp tiếp cận sử dụng Yocto Project, hãy xem xét những gợi ý dưới đây sau:

  * _Ghé qua website của Yocto Project:_ Website chính thức của [Yocto Project](http://www.yoctoproject.org) chứa thông tin về toàn bộ dự án. Ghé thăm website này là một cách tốt để cho bạn quen với toàn bộ dự án.

  * _Xem qua hướng dẫn phát triển Yocto Project:_ [Yocto Project Development Manual](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#dev-manual-intro) là nơi tuyệt vời để có cảm nhận sơ qua về việc sử dụng Yocto Project như thế nào. Tài liệu này chứa những thông tin khái niệm và mang tính thủ tục, nhưng bao phủ toàn bộ [common development models](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#dev-manual-model), giới thiệu về [the Yocto Project open source development environment](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#dev-manual-newbie). Tài liệu cũng giới thiệu một vài chương liên quan các task cụ thể [common tasks](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#extendpoky) như hiểu và tạo các layers, tùy biến Images, viết các recipes mới, làm việc với các thư viện libraries, cấu hình và thực hiện các bản vá (patching) cho kernel.

  * _Xem qua tài liệu về hướng dẫn phát triển bằng Yocto Project Software Development Kit (SDK):_[Yocto Project Software Development Kit (SDK) Developer's Guide](http://www.yoctoproject.org/docs/2.2/sdk-manual/sdk-manual.html#sdk-intro) miêu tả các sử dụng một SDK chuẩn [standard SDK](http://www.yoctoproject.org/docs/2.2/sdk-manual/sdk-manual.html#sdk-using-the-standard-sdk) và SDK mở rộng [extensible SDK](http://www.yoctoproject.org/docs/2.2/sdk-manual/sdk-manual.html#sdk-extensible), cái mà sẽ được sử dụng chủ yếu trong quá trình phát triển ứng dụng. Tài liệu này cũng cung cấp một ví dụ về luồng làm việc (workflow) IDE quen thuộc Eclipse™. Xem thêm tại chương "[Workflow using Eclipse™](http://www.yoctoproject.org/docs/2.2/sdk-manual/sdk-manual.html#workflow-using-eclipse)".

  * _Học thêm về gói hỗ trợ board (Board Support Packages (BSPs) ):_ Nếu bạn muốn biết thêm về các BSPs, hãy xem tài liệu [Yocto Project Board Support Packages (BSP) Developer's Guide](http://www.yoctoproject.org/docs/2.2/bsp-guide/bsp-guide.html#bsp).

  * _Học thêm về Toaster:_ Toaster là 1 giao diện web tương tác với môi trường build của Yocto Project hay OpenEmbedded. Nếu bạn muốn sử dụng loại giao diện này để tạo Image, hãy xem thêm [Toaster User Manual](http://www.yoctoproject.org/docs/2.2/toaster-manual/toaster-manual.html#toaster-manual-intro).

  * _Cuối cùng luôn có sẵn tài liệu tham khảo Yocto Project_ [Yocto Project Reference Manual](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#ref-manual-intro), không giống các tài liệu khác trong tập tài liệu của Yocto Project, nó bao gồm các tư liệu cho việc tham chiếu hơn là để sử dụng. Bạn có thể xem chi tiết tại [build details](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#usingpoky), hoặc kĩ hơn nữa [closer look](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#closer-look) về việc làm thế nào các thành phần của Yocto Project làm việc với nhau, cũng như thông tin về các vấn đề về kĩ thuật tại [technical details](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#technical-details), hướng dẫn chuyển đổi sang phiên bản mới [migrating to a newer Yocto Project release](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#migration), cấu trúc tham khảo [directory structure](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#ref-structure), [classes](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#ref-classes), and [tasks](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#ref-tasks). Tài liệu tham khảo Yocto Project cũng chứa những một tập toàn diện của các biến [glossary of variables](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#ref-variables-glossary) được sử dụng trong Yocto Project.