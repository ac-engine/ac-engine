
import aceutils

aceutils.cdToScript()
aceutils.mkdir('../Downloads')

with aceutils.CurrentDir('../Downloads'):
	aceutils.rmdir(r"bullet_bin")
	aceutils.rmdir(r"bullet_bin_x64")

	aceutils.editCmakeForACE(r'bullet3/CMakeLists.txt','cp932')
	aceutils.mkdir(r"bullet_bin")
	aceutils.mkdir(r"bullet_bin_x64")

	with aceutils.CurrentDir('bullet_bin'):
		if aceutils.isWin():
			aceutils.call(aceutils.cmd_cmake+r'-D USE_MSVC_RUNTIME_LIBRARY_DLL:BOOL=OFF -D BUILD_DEMOS:BOOL=OFF ../bullet3/')
			aceutils.call(aceutils.cmd_compile + r'BULLET_PHYSICS.sln /p:configuration=Debug')
			aceutils.call(aceutils.cmd_compile + r'BULLET_PHYSICS.sln /p:configuration=Release')
		elif aceutils.isMac():
			aceutils.call(r'cmake -G "Unix Makefiles" -D CMAKE_BUILD_TYPE=Release -D USE_MSVC_RUNTIME_LIBRARY_DLL:BOOL=OFF -D USE_INTERNAL_LOADER:BOOL=OFF -DBUILD_SHARED_LIBS=OFF -DBUILD_PYBULLET=OFF "-DCMAKE_OSX_ARCHITECTURES=x86_64' + (';i386' if aceutils.Isi386() else '') + r'" ../bullet3/')
			aceutils.call(r'make')
		else:
			aceutils.call(r'cmake -G "Unix Makefiles" -D CMAKE_BUILD_TYPE=Release -D USE_MSVC_RUNTIME_LIBRARY_DLL:BOOL=OFF ../bullet3/')
			aceutils.call(r'make')

	with aceutils.CurrentDir('bullet_bin_x64'):
		if aceutils.isWin():
			aceutils.call(aceutils.cmd_cmake_x64+r'-D USE_MSVC_RUNTIME_LIBRARY_DLL:BOOL=OFF -D BUILD_DEMOS:BOOL=OFF ../bullet3/')
			aceutils.call(aceutils.cmd_compile + r'BULLET_PHYSICS.sln /p:configuration=Debug')
			aceutils.call(aceutils.cmd_compile + r'BULLET_PHYSICS.sln /p:configuration=Release')

	aceutils.copytreeWithExt(r'bullet3/src/',r'../Dev/include/',['.h'])

	if aceutils.isWin():
		aceutils.mkdir(r'../Dev/lib/x86/')
		aceutils.mkdir(r'../Dev/lib/x86/Debug')
		aceutils.mkdir(r'../Dev/lib/x86/Release')

		aceutils.mkdir(r'../Dev/lib/x64/')
		aceutils.mkdir(r'../Dev/lib/x64/Debug')
		aceutils.mkdir(r'../Dev/lib/x64/Release')

		aceutils.copy(r'bullet_bin/lib/Debug/BulletCollision_Debug.lib', r'../Dev/lib/x86/Debug/')
		aceutils.copy(r'bullet_bin/lib/Debug/LinearMath_Debug.lib', r'../Dev/lib/x86/Debug/')

		aceutils.copy(r'bullet_bin/lib/Release/BulletCollision.lib', r'../Dev/lib/x86/Release/')
		aceutils.copy(r'bullet_bin/lib/Release/LinearMath.lib', r'../Dev/lib/x86/Release/')

		aceutils.copy(r'bullet_bin_x64/lib/Debug/BulletCollision_Debug.lib', r'../Dev/lib/x64/Debug/')
		aceutils.copy(r'bullet_bin_x64/lib/Debug/LinearMath_Debug.lib', r'../Dev/lib/x64/Debug/')

		aceutils.copy(r'bullet_bin_x64/lib/Release/BulletCollision.lib', r'../Dev/lib/x64/Release/')
		aceutils.copy(r'bullet_bin_x64/lib/Release/LinearMath.lib', r'../Dev/lib/x64/Release/')

	else:
		aceutils.copy(r'bullet_bin/src/BulletCollision/libBulletCollision.a', r'../Dev/lib/')
		aceutils.copy(r'bullet_bin/src/LinearMath/libLinearMath.a', r'../Dev/lib/')
