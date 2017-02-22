![](figures/yocto-project-transp.png)

## Yocto Project Quick Start¶

Copyright © 2010-2016 Linux Foundation

Permission is granted to copy, distribute and/or modify this document under
the terms of the [Creative Commons Attribution-Share Alike 2.0 UK: England &
Wales](http://creativecommons.org/licenses/by-sa/2.0/uk/) as published by
Creative Commons.

### Note

For the latest version of this manual associated with this Yocto Project
release, see the [Yocto Project Quick
Start](http://www.yoctoproject.org/docs/2.2/yocto-project-qs/yocto-project-
qs.html) from the Yocto Project website.

* * *

## Welcome!¶

Welcome to the Yocto Project! The Yocto Project is an open-source
collaboration project whose focus is developers of embedded Linux systems.
Among other things, the Yocto Project uses a build host based on the
OpenEmbedded (OE) project, which uses the
[BitBake](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html
#bitbake-term) tool, to construct complete Linux images. The BitBake and OE
components are combined together to form a reference build host, historically
known as [Poky](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-
manual.html#poky).

If you do not have a system that runs Linux and you want to give the Yocto
Project a test run, you might consider using the Yocto Project Build
Appliance. The Build Appliance allows you to build and boot a custom embedded
Linux image with the Yocto Project using a non-Linux development system. See
the [Yocto Project Build Appliance](https://www.yoctoproject.org/tools-
resources/projects/build-appliance) for more information.

This quick start is written so that you can quickly get a build host set up to
use the Yocto Project and then build some Linux images. Rather than go into
great detail about the Yocto Project and its many capabilities, this quick
start provides the minimal information you need to try out the Yocto Project
using a supported Linux build host. Reading and using the quick start should
result in you having a basic understanding of what the Yocto Project is and
how to use some of its core components. You will also have worked through
steps to produce two images: one that is suitable for emulation and one that
boots on actual hardware. The examples highlight the ease with which you can
use the Yocto Project to create images for multiple types of hardware.

For more detailed information on the Yocto Project, you can reference these
resources:

  * _Website:_ The [Yocto Project Website](http://www.yoctoproject.org) provides the latest builds, breaking news, full development documentation, and access to a rich Yocto Project Development Community into which you can tap. 

  * _FAQs:_ Lists commonly asked Yocto Project questions and answers. You can find two FAQs: [Yocto Project FAQ](https://wiki.yoctoproject.org/wiki/FAQ) on a wiki, and the "[FAQ](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#faq)" chapter in the Yocto Project Reference Manual. 

  * _Developer Screencast:_ The [Getting Started with the Yocto Project - New Developer Screencast Tutorial](http://vimeo.com/36450321) provides a 30-minute video created for users unfamiliar with the Yocto Project but familiar with Linux build hosts. While this screencast is somewhat dated, the introductory and fundamental concepts are useful for the beginner. 

## Introducing the Yocto Project Development Environment¶

The Yocto Project through the OpenEmbedded build system provides an open
source development environment targeting the ARM, MIPS, PowerPC, and x86
architectures for a variety of platforms including x86-64 and emulated ones.
You can use components from the Yocto Project to design, develop, build,
debug, simulate, and test the complete software stack using Linux, the X
Window System, GTK+ frameworks, and Qt frameworks.

![](figures/yocto-environment.png)

The Yocto Project Development Environment

Here are some highlights for the Yocto Project:

  * Provides a recent Linux kernel along with a set of system commands and libraries suitable for the embedded environment. 

  * Makes available system components such as X11, GTK+, Qt, Clutter, and SDL (among others) so you can create a rich user experience on devices that have display hardware. For devices that do not have a display or where you wish to use alternative UI frameworks, these components need not be installed. 

  * Creates a focused and stable core compatible with the OpenEmbedded project with which you can easily and reliably build and develop. 

  * Fully supports a wide range of hardware and device emulation through the Quick EMUlator (QEMU). 

  * Provides a layer mechanism that allows you to easily extend the system, make customizations, and keep them organized. 

You can use the Yocto Project to generate images for many kinds of devices. As
mentioned earlier, the Yocto Project supports creation of reference images
that you can boot within and emulate using QEMU. The standard example machines
target QEMU full-system emulation for 32-bit and 64-bit variants of x86, ARM,
MIPS, and PowerPC architectures. Beyond emulation, you can use the layer
mechanism to extend support to just about any platform that Linux can run on
and that a toolchain can target.

Another Yocto Project feature is the Sato reference User Interface. This
optional UI that is based on GTK+ is intended for devices with restricted
screen sizes and is included as part of the OpenEmbedded Core layer so that
developers can test parts of the software stack.

## Setting Up to Use the Yocto Project¶

The following list shows what you need in order to use a Linux-based build
host to use the Yocto Project to build images:

  * _Build Host_ A build host with a minimum of 50 Gbytes of free disk space that is running a supported Linux distribution (i.e. recent releases of Fedora, openSUSE, CentOS, Debian, or Ubuntu). 

  * _Build Host Packages_ Appropriate packages installed on the build host. 

  * _The Yocto Project_ A release of the Yocto Project. 

### The Linux Distribution¶

The Yocto Project team verifies each release against recent versions of the
most popular Linux distributions that provide stable releases. In general, if
you have the current release minus one of the following distributions, you
should have no problems.

  * Ubuntu 

  * Fedora 

  * openSUSE 

  * CentOS 

  * Debian 

For a more detailed list of distributions that support the Yocto Project, see
the "[Supported Linux Distributions](http://www.yoctoproject.org/docs/2.2/ref-
manual/ref-manual.html#detailed-supported-distros)" section in the Yocto
Project Reference Manual.

The OpenEmbedded build system should be able to run on any modern distribution
that has the following versions for Git, tar, and Python.

  * Git 1.8.3.1 or greater 

  * tar 1.24 or greater 

  * Python 3.4.0 or greater. 

If your build host does not meet any of these three listed version
requirements, you can take steps to prepare the system so that you can still
use the Yocto Project. See the "[Required Git, tar, and Python
Versions](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html
#required-git-tar-and-python-versions)" section in the Yocto Project Reference
Manual for information.

### The Build Host Packages¶

Required build host packages vary depending on your build machine and what you
want to do with the Yocto Project. For example, if you want to build an image
that can run on QEMU in graphical mode (a minimal, basic build requirement),
then the build host package requirements are different than if you want to
build an image on a headless system or build out the Yocto Project
documentation set.

Collectively, the number of required packages is large if you want to be able
to cover all cases.

### Note

In general, you need to have root access and then install the required
packages. Thus, the commands in the following section may or may not work
depending on whether or not your Linux distribution has `sudo` installed.

The following list shows the required packages needed to build an image that
runs on QEMU in graphical mode (e.g. essential plus graphics support). For
lists of required packages for other scenarios, see the "[Required Packages
for the Host Development System](http://www.yoctoproject.org/docs/2.2/ref-
manual/ref-manual.html#required-packages-for-the-host-development-system)"
section in the Yocto Project Reference Manual.

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
                            

### Note

CentOS 6.x users need to ensure that the required versions of Git, tar and
Python are available. For details, See the "[Required Git, tar, and Python
Versions](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html
#required-git-tar-and-python-versions)" section in the Yocto Project Reference
Manual for information.

### Yocto Project Release¶

The last requirement you need to meet before using the Yocto Project is
getting a Yocto Project release. It is recommended that you get the latest
Yocto Project release by setting up (cloning in
[Git](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#git)
terms) a local copy of the `poky` Git repository on your build host and then
checking out the latest release. Doing so allows you to easily update to newer
Yocto Project releases as well as contribute back to the Yocto Project.

Here is an example from an Ubuntu build host that clones the `poky` repository
and then checks out the latest Yocto Project Release (i.e. 2.2):

    
    
         $ git clone git://git.yoctoproject.org/poky
         Cloning into 'poky'...
         remote: Counting objects: 226790, done.
         remote: Compressing objects: 100% (57465/57465), done.
         remote: Total 226790 (delta 165212), reused 225887 (delta 164327)
         Receiving objects: 100% (226790/226790), 100.98 MiB | 263 KiB/s, done.
         Resolving deltas: 100% (165212/165212), done.
         $ git checkout morty
                    

You can also get the Yocto Project Files by downloading Yocto Project releases
from the [Yocto Project website](http://www.yoctoproject.org).

For more information on getting set up with the Yocto Project release, see the
"[Yocto Project Release](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-
manual.html#local-yp-release)" item in the Yocto Project Development Manual.

## Building Images¶

Now that you have your system requirements in order, you can give Yocto
Project a try. You can try out Yocto Project using either the command-line
interface or using Toaster, which uses a graphical user interface. If you want
to try out the Yocto Project using a GUI, see the [Toaster User
Manual](http://www.yoctoproject.org/docs/2.2/toaster-manual/toaster-
manual.html) for information on how to install and set up Toaster.

To use the Yocto Project through the command-line interface, finish this quick
start, which presents steps that let you do the following:

  * Build a `qemux86` reference image and run it in the QEMU emulator. 

  * Easily change configurations so that you can quickly create a second image that you can load onto bootable media and actually boot target hardware. This example uses the MinnowBoard MAX-compatible boards. 

### Note

The steps in the following two sections do not provide detail, but rather
provide minimal, working commands and examples designed to just get you
started. For more details, see the appropriate manuals in the [Yocto Project
manual set](http://www.yoctoproject.org/documentation).

### Building an Image for Emulation¶

Use the following commands to build your image. The OpenEmbedded build system
creates an entire Linux distribution, including the toolchain, from source.

### Note about Network Proxies

By default, the build process searches for source code using a pre-determined
order through a set of locations. If you are working behind a firewall and
your build host is not set up for proxies, you could encounter problems with
the build process when fetching source code (e.g. fetcher failures or Git
failures).

If you do not know your proxy settings, consult your local network
infrastructure resources and get that information. A good starting point could
also be to check your web browser settings. Finally, you can find more
information on using the Yocto Project behind a firewall in the Yocto Project
Reference Manual [FAQ](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-
manual.html#how-does-the-yocto-project-obtain-source-code-and-will-it-work-
behind-my-firewall-or-proxy-server) and on the "[Working Behind a Network
Proxy](https://wiki.yoctoproject.org/wiki/Working_Behind_a_Network_Proxy)"
wiki page.

  1. _Be Sure Your Build Host is Set Up:_ The steps to build an image in this section depend on your build host being properly set up. Be sure you have worked through the requirements described in the "Setting Up to Use the Yocto Project" section. 

  2. _Check Out Your Branch:_ Be sure you are in the [Source Directory](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#source-directory) (e.g. `poky`) and then check out the branch associated with the latest Yocto Project Release: 
    
    
         $ cd ~/poky
         $ git checkout -b morty origin/morty
                            

Git's `checkout` command checks out the current Yocto Project release into a
local branch whose name matches the release (i.e. `morty`). The local branch
tracks the upstream branch of the same name. Creating your own branch based on
the released branch ensures you are using the latest files for that release.

  3. _Initialize the Build Environment:_ Run the [`oe-init-build-env`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#structure-core-script) environment setup script to define the OpenEmbedded build environment on your build host. 
    
    
         $ source oe-init-build-env
                            

Among other things, the script creates the [Build
Directory](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html
#build-directory), which is `build` in this case and is located in the [Source
Directory](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html
#source-directory). After the script runs, your current working directory is
set to the Build Directory. Later, when the build completes, the Build
Directory contains all the files created during the build.

### Note

For information on running a memory-resident
[BitBake](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html
#usingpoky-components-bitbake), see the [`oe-init-build-env-
memres`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html
#structure-memres-core-script) setup script.

  4. _Examine Your Local Configuration File:_ When you set up the build environment, a local configuration file named `local.conf` becomes available in a `conf` subdirectory of the Build Directory. Before using BitBake to start the build, you can look at this file and be sure your general configurations are how you want them: 

    * To help conserve disk space during builds, you can add the following statement to your project's configuration file, which for this example is `poky/build/conf/local.conf`. Adding this statement deletes the work directory used for building a recipe once the recipe is built. 
    
    
         INHERIT += "rm_work"
                                    

    * By default, the target machine for the build is `qemux86`, which produces an image that can be used in the QEMU emulator and is targeted at an Intel® 32-bit based architecture. Further on in this example, this default is easily changed through the [`MACHINE`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-MACHINE) variable so that you can quickly build an image for a different machine. 

    * Another consideration before you build is the package manager used when creating the image. The default `local.conf` file selects the RPM package manager. You can control this configuration by using the `[`PACKAGE_CLASSES`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#var-PACKAGE_CLASSES)` variable.

Selection of the package manager is separate from whether package management
is used at runtime in the target image.

For additional package manager selection information, see the
"[`package.bbclass`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-
manual.html#ref-classes-package)" section in the Yocto Project Reference
Manual.

  5. _Start the Build:_ Continue with the following command to build an OS image for the target, which is `core-image-sato` in this example: 

### Note

Depending on the number of processors and cores, the amount of RAM, the speed
of your Internet connection and other factors, the build process could take
several hours the first time you run it. Subsequent builds run much faster
since parts of the build are cached.

    
    
         $ bitbake core-image-sato
                            

For information on using the `bitbake` command, see the
"[BitBake](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html
#usingpoky-components-bitbake)" section in the Yocto Project Reference Manual,
or see the "[BitBake Command](http://www.yoctoproject.org/docs/2.2/bitbake-
user-manual/bitbake-user-manual.html#bitbake-user-manual-command)" section in
the BitBake User Manual. For information on other targets, see the
"[Images](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#ref-
images)" chapter in the Yocto Project Reference Manual.

  6. _Simulate Your Image Using QEMU:_ Once this particular image is built, you can start QEMU and run the image: 
    
    
         $ runqemu qemux86
                            

If you want to learn more about running QEMU, see the "[Using the Quick
EMUlator (QEMU)](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-
manual.html#dev-manual-qemu)" chapter in the Yocto Project Development Manual.

  7. _Exit QEMU:_ Exit QEMU by either clicking on the shutdown icon or by opening a terminal, typing `poweroff`, and then pressing "Enter". 

### Building an Image for Hardware¶

The following steps show how easy it is to set up to build an image for a new
machine. These steps build an image for the MinnowBoard MAX, which is
supported by the Yocto Project and the `meta-intel` `intel-corei7-64` and
`intel-core2-32` Board Support Packages (BSPs).

### Note

The MinnowBoard MAX ships with 64-bit firmware. If you want to use the board
in 32-bit mode, you must download the [32-bit
firmware](http://firmware.intel.com/projects/minnowboard-max).

  1. _Create a Local Copy of the `meta-intel` Repository:_ Building an image for the MinnowBoard MAX requires the `meta-intel` layer. Use the `git clone` command to create a local copy of the repository inside your [Source Directory](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#source-directory), which is `poky` in this example: 
    
    
         $ cd $HOME/poky
         $ git clone git://git.yoctoproject.org/meta-intel
         Cloning into 'meta-intel'...
         remote: Counting objects: 11988, done.
         remote: Compressing objects: 100% (3884/3884), done.
         Receiving objects: 100% (11988/11988), 2.93 MiB | 2.51 MiB/s, done.
         remote: Total 11988 (delta 6881), reused 11752 (delta 6645)
         Resolving deltas: 100% (6881/6881), done.
         Checking connectivity... done.
                            

By default when you clone a Git repository, the "master" branch is checked
out. Before you build your image that uses the `meta-intel` layer, you must be
sure that both repositories (`meta-intel` and `poky`) are using the same
releases. Consequently, you need to checkout out the "`morty`" release after
cloning `meta-intel`:

    
    
         $ cd $HOME/poky/meta-intel
         $ git checkout morty
         Branch morty set up to track remote branch morty from origin.
         Switched to a new branch 'morty'
                            

  2. _Configure the Build:_ To configure the build, you edit the `bblayers.conf` and `local.conf` files, both of which are located in the `build/conf` directory. 

Here is a quick way to make the edits. The first command uses the `bitbake-
layers add-layer` command to add the `meta-intel` layer, which contains the
`intel-core*` BSPs to the build. The second command selects the BSP by setting
the [`MACHINE`](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-
manual.html#var-MACHINE) variable.

    
    
         $ cd $HOME/poky/build
         $ bitbake-layers add-layer "$HOME/poky/meta-intel"
         $ echo 'MACHINE = "intel-corei7-64"' >> conf/local.conf
                            

### Notes

If you want a 64-bit build, use the following:

    
    
         $ echo 'MACHINE = "intel-corei7-64"' >> conf/local.conf
                                

If you want 32-bit images, use the following:

    
    
         $ echo 'MACHINE = "intel-core2-32"' >> conf/local.conf
                                

  3. _Build an Image for MinnowBoard MAX:_ The type of image you build depends on your goals. For example, the previous build created a `core-image-sato` image, which is an image with Sato support. It is possible to build many image types for the MinnowBoard MAX. Some possibilities are `core-image-base`, which is a console-only image. Another choice could be a `core-image-full-cmdline`, which is another console-only image but has more full-features Linux system functionality installed. For types of images you can build using the Yocto Project, see the "[Images](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#ref-images)" chapter in the Yocto Project Reference Manual.

Because configuration changes are minimal to set up for this second build, the
OpenEmbedded build system can re-use files from previous builds as much as
possible. Re-using files means this second build will be much faster than an
initial build. For this example, the `core-image-base` image is built:

    
    
         $ bitbake core-image-base
                            

Once the build completes, the resulting console-only image is located in the
Build Directory here:

    
    
         tmp/deploy/images/intel-corei7-64/core-image-base-intel-corei7-64.wic
                            

  4. _Write the Image:_ You can write the image just built to a bootable media (e.g. a USB key, SATA drive, SD card, etc.) using the `dd` utility: 
    
    
         $ sudo dd if=tmp/deploy/images/intel-corei7-64/core-image-base-intel-corei7-64.wic of=TARGET_DEVICE
                            

In the previous command, the `TARGET_DEVICE` is the device node in the host
machine (e.g. `/dev/sdc`, which is most likely a USB stick, or `/dev/mmcblk0`,
which is most likely an SD card).

  5. _Boot the Hardware:_ With the boot device provisioned, you can insert the media into the MinnowBoard MAX and boot the hardware. The board should automatically detect the media and boot to the bootloader and subsequently the operating system. 

If the board does not boot automatically, you can boot it manually from the
EFI shell as follows:

    
    
         Shell> connect -r
         Shell> map -r
         Shell> fs0:
         Shell> bootx64
                            

### Note

For a 32-bit image use the following:

    
    
         Shell> bootia32
                                

## Next Steps¶

If you completed all the steps in the previous section then congratulations!
What now?

Depending on what you primary interests are with the Yocto Project, you could
consider any of the following:

  * _Visit the Yocto Project Web Site:_ The official [Yocto Project](http://www.yoctoproject.org) web site contains information on the entire project. Visiting this site is a good way to familiarize yourself with the overall project. 

  * _Look Through the Yocto Project Development Manual:_ The [Yocto Project Development Manual](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#dev-manual-intro) is a great place to get a feel for how to use the Yocto Project. The manual contains conceptual and procedural information that covers [common development models](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#dev-manual-model) and introduces [the Yocto Project open source development environment](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#dev-manual-newbie). The manual also contains several targeted sections that cover specific [common tasks](http://www.yoctoproject.org/docs/2.2/dev-manual/dev-manual.html#extendpoky) such as understanding and creating layers, customizing images, writing new recipes, working with libraries, and configuring and patching the kernel. 

  * _Look Through the Yocto Project Software Development Kit (SDK) Developer's Guide:_ The [Yocto Project Software Development Kit (SDK) Developer's Guide](http://www.yoctoproject.org/docs/2.2/sdk-manual/sdk-manual.html#sdk-intro) describes how to use both the [standard SDK](http://www.yoctoproject.org/docs/2.2/sdk-manual/sdk-manual.html#sdk-using-the-standard-sdk) and the [extensible SDK](http://www.yoctoproject.org/docs/2.2/sdk-manual/sdk-manual.html#sdk-extensible), which are used primarily for application development. This manual also provides an example workflow that uses the popular Eclipse™ development environment. See the "[Workflow using Eclipse™](http://www.yoctoproject.org/docs/2.2/sdk-manual/sdk-manual.html#workflow-using-eclipse)" section. 

  * _Learn About Board Support Packages (BSPs):_ If you want to learn about BSPs, see the [Yocto Project Board Support Packages (BSP) Developer's Guide](http://www.yoctoproject.org/docs/2.2/bsp-guide/bsp-guide.html#bsp). 

  * _Learn About Toaster:_ Toaster is a web interface to the Yocto Project's OpenEmbedded build system. If you are interested in using this type of interface to create images, see the [Toaster User Manual](http://www.yoctoproject.org/docs/2.2/toaster-manual/toaster-manual.html#toaster-manual-intro). 

  * _Have Available the Yocto Project Reference Manual_ The [Yocto Project Reference Manual](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#ref-manual-intro), unlike the rest of the Yocto Project manual set, is comprised of material suited for reference rather than procedures. You can get [build details](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#usingpoky), a [closer look](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#closer-look) at how the pieces of the Yocto Project development environment work together, information on various [technical details](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#technical-details), guidance on [migrating to a newer Yocto Project release](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#migration), reference material on the [directory structure](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#ref-structure), [classes](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#ref-classes), and [tasks](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#ref-tasks). The Yocto Project Reference Manual also contains a fairly comprehensive [glossary of variables](http://www.yoctoproject.org/docs/2.2/ref-manual/ref-manual.html#ref-variables-glossary) used within the Yocto Project. 

