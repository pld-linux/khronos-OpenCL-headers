Summary:	OpenCL (Open Computing Language) header files
Summary(pl.UTF-8):	Pliki nagłówkowe OpenCL (Open Computing Language)
Name:		khronos-OpenCL-headers
Version:	2.2
Release:	1
License:	MIT-like
Group:		Libraries
Source0:	https://raw.githubusercontent.com/KhronosGroup/OpenCL-Headers/master/opencl22/CL/cl.h
# Source0-md5:	98f9e8ebab9d3baf4b9b7d004a682eca
Source1:	https://raw.githubusercontent.com/KhronosGroup/OpenCL-Headers/master/opencl22/CL/cl_egl.h
# Source1-md5:	c7f42a37356c2d4e42f2692921ed09a7
Source2:	https://raw.githubusercontent.com/KhronosGroup/OpenCL-Headers/master/opencl22/CL/cl_ext.h
# Source2-md5:	0be05487e184ac36cf789d3badfdede2
Source3:	https://raw.githubusercontent.com/KhronosGroup/OpenCL-Headers/master/opencl22/CL/cl_gl.h
# Source3-md5:	b1dac507ba9b9abf0d6060f4acd5f414
Source4:	https://raw.githubusercontent.com/KhronosGroup/OpenCL-Headers/master/opencl22/CL/cl_gl_ext.h
# Source4-md5:	8982a32bca3c81bfab06c265e0a4130e
Source5:	https://raw.githubusercontent.com/KhronosGroup/OpenCL-Headers/master/opencl22/CL/cl_platform.h
# Source5-md5:	dbc6a23be143d0cb586f605fd39741d5
Source6:	https://raw.githubusercontent.com/KhronosGroup/OpenCL-Headers/master/opencl22/CL/opencl.h
# Source6-md5:	687394644e8c4ec4fd3d77f2f86bc042
# Three following are Win32 specific (rely on D3D), so we don't package them:
#Source11:	https://raw.githubusercontent.com/KhronosGroup/OpenCL-Headers/master/opencl22/CL/cl_d3d10.h
## Source11-md5:	64634186074ea8570ea24ce50b328968
#Source12:	https://raw.githubusercontent.com/KhronosGroup/OpenCL-Headers/master/opencl22/CL/cl_d3d11.h
## Source12-md5:	2608ee0f7a6101216cdfe3046591da30
#Source13:	https://raw.githubusercontent.com/KhronosGroup/OpenCL-Headers/master/opencl22/CL/cl_dx9_media_sharing.h
## Source13-md5:	6d92fb282cab5cfa91aa05d62ed1953e
# This actually belongs to OpenCL 1.2, included for backward compatibility (OpenCL 2+ uses cl2.hpp)
Source50:	https://www.khronos.org/registry/cl/api/2.1/cl.hpp
# Source50-md5:	f2c8bee05e5a84ea8282b7b95646c515
# OpenCL 2+ binding from CLHPP project
#Source51Download: https://www.github.com/KhronosGroup/OpenCL-CLHPP/releases
Source51:	https://github.com/KhronosGroup/OpenCL-CLHPP/releases/download/v2.0.10/cl2.hpp
# Source51-md5:	c38d1b78cd98cc809fa2a49dbd1734a5
Patch0:		AMD_extensions.patch
URL:		http://www.khronos.org/registry/cl/
Conflicts:	Mesa-libOpenCL-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenCL (Open Computing Language) header files.

%description -l pl.UTF-8
Pliki nagłówkowe języka obliczeń OpenCL (Open Computing Language).

%prep
%setup -q -cT

cp %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} \
	%{SOURCE50} %{SOURCE51} .

%patch -P0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/CL
cp -p *.h cl.hpp cl2.hpp $RPM_BUILD_ROOT%{_includedir}/CL

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_includedir}/CL
