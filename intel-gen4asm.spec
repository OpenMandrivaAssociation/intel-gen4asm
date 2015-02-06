Name: intel-gen4asm
Version: 20100209
Release: 3
Summary: a program to compile an assembly language for the Intel 965
Group: Development/X11
# git archive --format=tar --prefix=intel-gen4asm/ master | bzip2 > intel-gen4asm.tar.bz2
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
%{_bindir}/intel-gen4disasm
%{_libdir}/pkgconfig/intel-gen4asm.pc


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 20100209-2mdv2011.0
+ Revision: 612399
- the mass rebuild of 2010.1 packages

* Tue Feb 09 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 20100209-1mdv2010.1
+ Revision: 503274
- Update to the most recent git checkout

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild early 2009.0 package (before pixel changes)

* Wed Apr 16 2008 Paulo Andrade <pcpa@mandriva.com.br> 20081516-2mdv2009.0
+ Revision: 194864
- intel-gen4asm is a program to compile an assembly language for the Intel 965
  Express Chipset.  It has been used to construct programs for textured video in
  the 2d driver.
- intel-gen4asm package.

