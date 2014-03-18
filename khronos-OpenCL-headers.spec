Summary:	OpenCL (Open Computing Language) header files
Name:		khronos-OpenCL-headers
Version:	1.2
Release:	0.1
License:	MIT-like
Group:		Libraries
Source0:	http://www.khronos.org/registry/cl/api/1.2/cl.h
# Source0-md5:	393ecb00c9a15a2a942e135fd4eb4b82
Source1:	http://www.khronos.org/registry/cl/api/1.2/cl.hpp
# Source1-md5:	c364c5b654af266fc53711305357419f
Source2:	http://www.khronos.org/registry/cl/api/1.2/cl_egl.h
# Source2-md5:	7b8446dab1d765ebde0a23095971ac89
Source3:	http://www.khronos.org/registry/cl/api/1.2/cl_ext.h
# Source3-md5:	d5630fb0dc6fb6e9f3b679f26a80a075
Source4:	http://www.khronos.org/registry/cl/api/1.2/cl_gl.h
# Source4-md5:	b8429948c35e43d72f944a4d732967e5
Source5:	http://www.khronos.org/registry/cl/api/1.2/cl_gl_ext.h
# Source5-md5:	9e389c6edecc8559ca9b861ed3e8e96b
Source6:	http://www.khronos.org/registry/cl/api/1.2/cl_platform.h
# Source6-md5:	360ac18b454f86e93a63afda1c3061e2
Source7:	http://www.khronos.org/registry/cl/api/1.2/opencl.h
# Source7-md5:	6f511443ae9d2f85146e0c35221c1e7d
# Those rely on D3D:
# SourceXX:	http://www.khronos.org/registry/cl/api/1.2/cl_d3d10.h
## SourceXX-md5:	733d5d6b54cebdd0ecdde27e341bd465
#SourceXX:	http://www.khronos.org/registry/cl/api/1.2/cl_d3d11.h
## SourceXX-md5:	f53b2ffef7d9197fcc3cf80df2059d35
#SourceXX:	http://www.khronos.org/registry/cl/api/1.2/cl_dx9_media_sharing.h
## SourceXX-md5:	1ad86f41fd01f3ba0388f5b610e65a07
URL:		http://www.khronos.org/registry/cl/
Provides:	OpenCL-devel = 1.2
Obsoletes:	Mesa-libOpenCL-devel
Conflicts:	Mesa-libOpenCL-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenCL (Open Computing Language) header files.

%prep
%setup -q -cT
cp %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} \
	%{SOURCE5} %{SOURCE6} %{SOURCE7} .

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/CL
install *.h $RPM_BUILD_ROOT%{_includedir}/CL

%files
%defattr(644,root,root,755)
%{_includedir}/CL

%clean
rm -rf $RPM_BUILD_ROOT
