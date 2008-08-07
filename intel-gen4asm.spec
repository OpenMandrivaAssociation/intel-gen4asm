Name: intel-gen4asm
Version: 20080416
Release: %mkrel 4
Summary: a program to compile an assembly language for the Intel 965
Group: Development/X11
# git-archive --format=tar --prefix=intel-gen4asm/ master | bzip2 > intel-gen4asm.tar.bz2
Source: intel-gen4asm.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: flex bison

%description
intel-gen4asm is a program to compile an assembly language for the Intel 965
Express Chipset.  It has been used to construct programs for textured video in
the 2d driver.

%prep
%setup -q -n %{name}

%build
sh autogen.sh

%configure

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/intel-gen4asm
