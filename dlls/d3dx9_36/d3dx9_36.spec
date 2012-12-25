@ stdcall D3DXAssembleShader(ptr long ptr ptr long ptr ptr)
@ stdcall D3DXAssembleShaderFromFileA(str ptr ptr long ptr ptr)
@ stdcall D3DXAssembleShaderFromFileW(wstr ptr ptr long ptr ptr)
@ stdcall D3DXAssembleShaderFromResourceA(long str ptr ptr long ptr ptr)
@ stdcall D3DXAssembleShaderFromResourceW(long wstr ptr ptr long ptr ptr)
@ stdcall D3DXBoxBoundProbe(ptr ptr ptr ptr)
@ stdcall D3DXCheckCubeTextureRequirements(ptr ptr ptr long ptr ptr)
@ stdcall D3DXCheckTextureRequirements(ptr ptr ptr ptr long ptr ptr)
@ stdcall D3DXCheckVersion(long long)
@ stdcall D3DXCheckVolumeTextureRequirements(ptr ptr ptr ptr ptr long ptr ptr)
@ stdcall D3DXCleanMesh(long ptr ptr ptr ptr ptr)
@ stdcall D3DXColorAdjustContrast(ptr ptr float)
@ stdcall D3DXColorAdjustSaturation(ptr ptr float)
@ stdcall D3DXCompileShader(ptr long ptr ptr str str long ptr ptr ptr)
@ stdcall D3DXCompileShaderFromFileA(str ptr ptr str str long ptr ptr ptr)
@ stdcall D3DXCompileShaderFromFileW(wstr ptr ptr str str long ptr ptr ptr)
@ stdcall D3DXCompileShaderFromResourceA(ptr str ptr ptr str str long ptr ptr ptr)
@ stdcall D3DXCompileShaderFromResourceW(ptr wstr ptr ptr str str long ptr ptr ptr)
@ stdcall D3DXComputeBoundingBox(ptr long long ptr ptr)
@ stdcall D3DXComputeBoundingSphere(ptr long long ptr ptr)
@ stub D3DXComputeIMTFromPerVertexSignal(ptr ptr long long long ptr ptr ptr)
@ stub D3DXComputeIMTFromPerTexelSignal(ptr long ptr long long long long long ptr ptr ptr)
@ stub D3DXComputeIMTFromSignal(ptr long long long long ptr ptr ptr ptr ptr)
@ stub D3DXComputeIMTFromTexture(ptr ptr long long ptr ptr ptr)
@ stub D3DXComputeNormalMap(ptr ptr ptr long long long)
@ stub D3DXComputeNormals(ptr ptr)
@ stub D3DXComputeTangent(ptr long long long long ptr)
@ stub D3DXComputeTangentFrame(ptr long)
@ stub D3DXComputeTangentFrameEx(ptr long long long long long long long long long ptr long long long ptr ptr)
@ stub D3DXConcatenateMeshes(ptr long long ptr ptr ptr ptr ptr)
@ stub D3DXConvertMeshSubsetToSingleStrip(ptr long long ptr ptr)
@ stub D3DXConvertMeshSubsetToStrips(ptr long long ptr ptr ptr ptr)
@ stub D3DXCreateAnimationController(long long long long ptr)
@ stdcall D3DXCreateBox(ptr float float float ptr ptr)
@ stdcall D3DXCreateBuffer(long ptr)
@ stub D3DXCreateCompressedAnimationSet(ptr long long ptr long ptr ptr)
@ stdcall D3DXCreateCubeTexture(ptr long long long long long ptr)
@ stdcall D3DXCreateCubeTextureFromFileA(ptr ptr ptr)
@ stdcall D3DXCreateCubeTextureFromFileExA(ptr ptr long long long long long long long long ptr ptr ptr)
@ stdcall D3DXCreateCubeTextureFromFileExW(ptr ptr long long long long long long long long ptr ptr ptr)
@ stdcall D3DXCreateCubeTextureFromFileInMemory(ptr ptr long ptr)
@ stdcall D3DXCreateCubeTextureFromFileInMemoryEx(ptr ptr long long long long long long long long long ptr ptr ptr)
@ stdcall D3DXCreateCubeTextureFromFileW(ptr ptr ptr)
@ stub D3DXCreateCubeTextureFromResourceA(ptr long ptr ptr)
@ stub D3DXCreateCubeTextureFromResourceExA(ptr long long long long long long long long long long ptr ptr ptr)
@ stub D3DXCreateCubeTextureFromResourceExW(ptr long long long long long long long long long long ptr ptr ptr)
@ stub D3DXCreateCubeTextureFromResourceW(ptr long ptr ptr)
@ stdcall D3DXCreateCylinder(ptr long long long long long ptr ptr)
@ stdcall D3DXCreateEffect(ptr ptr long ptr ptr long ptr ptr ptr)
@ stdcall D3DXCreateEffectCompiler(ptr long ptr ptr long ptr ptr)
@ stdcall D3DXCreateEffectCompilerFromFileA(str ptr ptr long ptr ptr)
@ stdcall D3DXCreateEffectCompilerFromFileW(wstr ptr ptr long ptr ptr)
@ stdcall D3DXCreateEffectCompilerFromResourceA(long str ptr ptr long ptr ptr)
@ stdcall D3DXCreateEffectCompilerFromResourceW(long wstr ptr ptr long ptr ptr)
@ stdcall D3DXCreateEffectEx(ptr ptr long ptr ptr str long ptr ptr ptr)
@ stdcall D3DXCreateEffectFromFileA(ptr str ptr ptr long ptr ptr ptr)
@ stdcall D3DXCreateEffectFromFileExA(ptr str ptr ptr str long ptr ptr ptr)
@ stdcall D3DXCreateEffectFromFileExW(ptr str ptr ptr str long ptr ptr ptr)
@ stdcall D3DXCreateEffectFromFileW(ptr wstr ptr ptr long ptr ptr ptr)
@ stdcall D3DXCreateEffectFromResourceA(ptr long str ptr ptr long ptr ptr ptr)
@ stdcall D3DXCreateEffectFromResourceExA(ptr long str ptr ptr str long ptr ptr ptr)
@ stdcall D3DXCreateEffectFromResourceExW(ptr long str ptr ptr str long ptr ptr ptr)
@ stdcall D3DXCreateEffectFromResourceW(ptr long wstr ptr ptr long ptr ptr ptr)
@ stdcall D3DXCreateEffectPool(ptr)
@ stdcall D3DXCreateFontA(ptr long long long long long long long long long str ptr)
@ stdcall D3DXCreateFontIndirectA(ptr ptr ptr)
@ stdcall D3DXCreateFontIndirectW(ptr ptr ptr)
@ stdcall D3DXCreateFontW(ptr long long long long long long long long long wstr ptr)
@ stub D3DXCreateFragmentLinker(ptr long ptr)
@ stub D3DXCreateFragmentLinkerEx(ptr long long ptr)
@ stub D3DXCreateKeyframedAnimationSet(ptr long long long long ptr ptr)
@ stdcall D3DXCreateLine(ptr ptr)
@ stdcall D3DXCreateMatrixStack(long ptr)
@ stdcall D3DXCreateMesh(long long long ptr ptr ptr)
@ stdcall D3DXCreateMeshFVF(long long long long ptr ptr)
@ stub D3DXCreateNPatchMesh(ptr ptr)
@ stub D3DXCreatePMeshFromStream(ptr long ptr ptr ptr ptr ptr)
@ stub D3DXCreatePatchMesh(ptr long long long ptr ptr ptr)
@ stub D3DXCreatePolygon(ptr long long ptr ptr)
@ stub D3DXCreatePRTBuffer(long long long ptr)
@ stub D3DXCreatePRTBufferTex(long long long long ptr)
@ stub D3DXCreatePRTCompBuffer(long long long ptr ptr ptr ptr)
@ stub D3DXCreatePRTEngine(ptr ptr long ptr ptr)
@ stdcall D3DXCreateRenderToEnvMap(ptr long long long long long ptr)
@ stdcall D3DXCreateRenderToSurface(ptr long long long long long ptr)
@ stub D3DXCreateSPMesh(ptr ptr ptr ptr ptr)
@ stdcall D3DXCreateSkinInfo(long ptr long ptr)
@ stub D3DXCreateSkinInfoFromBlendedMesh(ptr long ptr ptr)
@ stdcall D3DXCreateSkinInfoFVF(long long long ptr)
@ stdcall D3DXCreateSphere(ptr float long long ptr ptr)
@ stdcall D3DXCreateSprite(ptr ptr)
@ stdcall D3DXCreateTeapot(ptr ptr ptr)
@ stdcall D3DXCreateTextA(ptr long str float float ptr ptr ptr)
@ stdcall D3DXCreateTextW(ptr long wstr float float ptr ptr ptr)
@ stdcall D3DXCreateTexture(ptr long long long long long long ptr)
@ stdcall D3DXCreateTextureFromFileA(ptr str ptr)
@ stdcall D3DXCreateTextureFromFileExA(ptr str long long long long long long long long long ptr ptr ptr)
@ stdcall D3DXCreateTextureFromFileExW(ptr wstr long long long long long long long long long ptr ptr ptr)
@ stdcall D3DXCreateTextureFromFileInMemory(ptr ptr long ptr)
@ stdcall D3DXCreateTextureFromFileInMemoryEx(ptr ptr long long long long long long long long long long ptr ptr ptr)
@ stdcall D3DXCreateTextureFromFileW(ptr wstr ptr)
@ stdcall D3DXCreateTextureFromResourceA(ptr ptr str ptr)
@ stdcall D3DXCreateTextureFromResourceExA(ptr ptr str long long long long long long long long long ptr ptr ptr)
@ stdcall D3DXCreateTextureFromResourceExW(ptr ptr wstr long long long long long long long long long ptr ptr ptr)
@ stdcall D3DXCreateTextureFromResourceW(ptr ptr wstr ptr)
@ stub D3DXCreateTextureGutterHelper(long long ptr long ptr)
@ stub D3DXCreateTextureShader(ptr ptr)
@ stub D3DXCreateTorus(ptr long long long long ptr ptr)
@ stdcall D3DXCreateVolumeTexture(ptr long long long long long long long ptr)
@ stdcall D3DXCreateVolumeTextureFromFileA(ptr ptr ptr)
@ stdcall D3DXCreateVolumeTextureFromFileExA(ptr ptr long long long long long long long long long long ptr ptr ptr)
@ stdcall D3DXCreateVolumeTextureFromFileExW(ptr ptr long long long long long long long long long long ptr ptr ptr)
@ stdcall D3DXCreateVolumeTextureFromFileInMemory(ptr ptr long ptr)
@ stdcall D3DXCreateVolumeTextureFromFileInMemoryEx(ptr ptr long long long long long long long long long long long ptr ptr ptr)
@ stdcall D3DXCreateVolumeTextureFromFileW(ptr ptr ptr)
@ stub D3DXCreateVolumeTextureFromResourceA(ptr long ptr ptr)
@ stub D3DXCreateVolumeTextureFromResourceExA(ptr long ptr long long long long long long long long long long ptr ptr ptr)
@ stub D3DXCreateVolumeTextureFromResourceExW(ptr long ptr long long long long long long long long long long ptr ptr ptr)
@ stub D3DXCreateVolumeTextureFromResourceW(ptr long ptr ptr)
@ stdcall D3DXDebugMute(long)
@ stdcall D3DXDeclaratorFromFVF(long ptr)
@ stub D3DXDisassembleEffect(ptr long ptr)
@ stub D3DXDisassembleShader(ptr long ptr ptr)
@ stdcall D3DXFileCreate(ptr)
@ stdcall D3DXFillCubeTexture(ptr ptr ptr)
@ stub D3DXFillCubeTextureTX(ptr ptr)
@ stdcall D3DXFillTexture(ptr ptr ptr)
@ stub D3DXFillTextureTX(ptr ptr)
@ stdcall D3DXFillVolumeTexture(ptr ptr ptr)
@ stub D3DXFillVolumeTextureTX(ptr ptr)
@ stdcall D3DXFilterTexture(ptr ptr long long)
@ stdcall D3DXFindShaderComment(ptr long ptr ptr)
@ stdcall D3DXFloat16To32Array(ptr ptr long)
@ stdcall D3DXFloat32To16Array(ptr ptr long)
@ stub D3DXFrameAppendChild(ptr ptr)
@ stub D3DXFrameCalculateBoundingSphere(ptr ptr ptr)
@ stdcall D3DXFrameDestroy(ptr ptr)
@ stub D3DXFrameFind(ptr ptr)
@ stub D3DXFrameNumNamedMatrices(ptr)
@ stub D3DXFrameRegisterNamedMatrices(ptr ptr)
@ stdcall D3DXFresnelTerm(float float)
@ stdcall D3DXFVFFromDeclarator(ptr ptr)
@ stub D3DXGatherFragments(ptr long ptr ptr long ptr ptr)
@ stub D3DXGatherFragmentsFromFileA(ptr ptr ptr long ptr ptr)
@ stub D3DXGatherFragmentsFromFileW(ptr ptr ptr long ptr ptr)
@ stub D3DXGatherFragmentsFromResourceA(long ptr ptr ptr long ptr ptr)
@ stub D3DXGatherFragmentsFromResourceW(long ptr ptr ptr long ptr ptr)
@ stub D3DXGenerateOutputDecl(ptr ptr)
@ stub D3DXGeneratePMesh(ptr ptr ptr ptr long long ptr)
@ stdcall D3DXGetDeclLength(ptr)
@ stdcall D3DXGetDeclVertexSize(ptr long)
@ stdcall D3DXGetDriverLevel(ptr)
@ stdcall D3DXGetFVFVertexSize(long)
@ stdcall D3DXGetImageInfoFromFileA(str ptr)
@ stdcall D3DXGetImageInfoFromFileInMemory(ptr long ptr)
@ stdcall D3DXGetImageInfoFromFileW(wstr ptr)
@ stdcall D3DXGetImageInfoFromResourceA(long str ptr)
@ stdcall D3DXGetImageInfoFromResourceW(long wstr ptr)
@ stdcall D3DXGetPixelShaderProfile(ptr)
@ stdcall D3DXGetShaderConstantTable(ptr ptr)
@ stdcall D3DXGetShaderConstantTableEx(ptr long ptr)
@ stub D3DXGetShaderInputSemantics(ptr ptr ptr)
@ stub D3DXGetShaderOutputSemantics(ptr ptr ptr)
@ stdcall D3DXGetShaderSamplers(ptr ptr ptr)
@ stdcall D3DXGetShaderSize(ptr)
@ stdcall D3DXGetShaderVersion(ptr)
@ stdcall D3DXGetVertexShaderProfile(ptr)
@ stub D3DXIntersect(ptr ptr ptr ptr ptr ptr ptr ptr ptr ptr)
@ stub D3DXIntersectSubset(ptr long ptr ptr ptr ptr ptr ptr ptr ptr ptr)
@ stdcall D3DXIntersectTri(ptr ptr ptr ptr ptr ptr ptr ptr)
@ stdcall D3DXLoadMeshFromXA(str long ptr ptr ptr ptr ptr ptr)
@ stdcall D3DXLoadMeshFromXInMemory(ptr long long ptr ptr ptr ptr ptr ptr)
@ stdcall D3DXLoadMeshFromXResource(long str str long ptr ptr ptr ptr ptr ptr)
@ stdcall D3DXLoadMeshFromXW(wstr long ptr ptr ptr ptr ptr ptr)
@ stub D3DXLoadMeshFromXof(ptr long ptr ptr ptr ptr ptr ptr)
@ stdcall D3DXLoadMeshHierarchyFromXA(str long ptr ptr ptr ptr ptr)
@ stdcall D3DXLoadMeshHierarchyFromXInMemory(ptr long long ptr ptr ptr ptr ptr)
@ stdcall D3DXLoadMeshHierarchyFromXW(wstr long ptr ptr ptr ptr ptr)
@ stub D3DXLoadPatchMeshFromXof(ptr long ptr ptr ptr long ptr)
@ stub D3DXLoadPRTBufferFromFileA(ptr ptr)
@ stub D3DXLoadPRTBufferFromFileW(ptr ptr)
@ stub D3DXLoadPRTCompBufferFromFileA(ptr ptr)
@ stub D3DXLoadPRTCompBufferFromFileW(ptr ptr)
@ stub D3DXLoadSkinMeshFromXof(ptr long ptr ptr ptr ptr ptr ptr ptr)
@ stdcall D3DXLoadSurfaceFromFileA(ptr ptr ptr str ptr long long ptr)
@ stdcall D3DXLoadSurfaceFromFileInMemory(ptr ptr ptr ptr long ptr long long ptr)
@ stdcall D3DXLoadSurfaceFromFileW(ptr ptr ptr wstr ptr long long ptr)
@ stdcall D3DXLoadSurfaceFromMemory(ptr ptr ptr ptr long long ptr ptr long long)
@ stdcall D3DXLoadSurfaceFromResourceA(ptr ptr ptr ptr str ptr long long ptr)
@ stdcall D3DXLoadSurfaceFromResourceW(ptr ptr ptr ptr wstr ptr long long ptr)
@ stdcall D3DXLoadSurfaceFromSurface(ptr ptr ptr ptr ptr ptr long long)
@ stdcall D3DXLoadVolumeFromFileA(ptr ptr ptr ptr ptr long long ptr)
@ stdcall D3DXLoadVolumeFromFileInMemory(ptr ptr ptr ptr long ptr long long ptr)
@ stdcall D3DXLoadVolumeFromFileW(ptr ptr ptr ptr ptr long long ptr)
@ stdcall D3DXLoadVolumeFromMemory(ptr ptr ptr ptr long long long ptr ptr long long)
@ stub D3DXLoadVolumeFromResourceA(ptr ptr ptr long ptr ptr long long ptr)
@ stub D3DXLoadVolumeFromResourceW(ptr ptr ptr long ptr ptr long long ptr)
@ stdcall D3DXLoadVolumeFromVolume(ptr ptr ptr ptr ptr ptr long long)
@ stdcall D3DXMatrixAffineTransformation(ptr float ptr ptr ptr)
@ stdcall D3DXMatrixAffineTransformation2D(ptr float ptr float ptr)
@ stdcall D3DXMatrixDecompose(ptr ptr ptr ptr)
@ stdcall D3DXMatrixDeterminant(ptr)
@ stdcall D3DXMatrixInverse(ptr ptr ptr)
@ stdcall D3DXMatrixLookAtLH(ptr ptr ptr ptr)
@ stdcall D3DXMatrixLookAtRH(ptr ptr ptr ptr)
@ stdcall D3DXMatrixMultiply(ptr ptr ptr)
@ stdcall D3DXMatrixMultiplyTranspose(ptr ptr ptr)
@ stdcall D3DXMatrixOrthoLH(ptr float float float float)
@ stdcall D3DXMatrixOrthoOffCenterLH(ptr float float float float float float)
@ stdcall D3DXMatrixOrthoOffCenterRH(ptr float float float float float float)
@ stdcall D3DXMatrixOrthoRH(ptr float float float float)
@ stdcall D3DXMatrixPerspectiveFovLH(ptr float float float float)
@ stdcall D3DXMatrixPerspectiveFovRH(ptr float float float float)
@ stdcall D3DXMatrixPerspectiveLH(ptr float float float float)
@ stdcall D3DXMatrixPerspectiveOffCenterLH(ptr float float float float float float)
@ stdcall D3DXMatrixPerspectiveOffCenterRH(ptr float float float float float float)
@ stdcall D3DXMatrixPerspectiveRH(ptr float float float float)
@ stdcall D3DXMatrixReflect(ptr ptr)
@ stdcall D3DXMatrixRotationAxis(ptr ptr float)
@ stdcall D3DXMatrixRotationQuaternion(ptr ptr)
@ stdcall D3DXMatrixRotationX(ptr float)
@ stdcall D3DXMatrixRotationY(ptr float)
@ stdcall D3DXMatrixRotationYawPitchRoll(ptr float float float)
@ stdcall D3DXMatrixRotationZ(ptr float)
@ stdcall D3DXMatrixScaling(ptr float float float)
@ stdcall D3DXMatrixShadow(ptr ptr ptr)
@ stdcall D3DXMatrixTransformation(ptr ptr ptr ptr ptr ptr ptr)
@ stdcall D3DXMatrixTransformation2D(ptr ptr float ptr ptr float ptr)
@ stdcall D3DXMatrixTranslation(ptr float float float)
@ stdcall D3DXMatrixTranspose(ptr ptr)
@ stdcall D3DXOptimizeFaces(ptr long long long ptr)
@ stub D3DXOptimizeVertices(ptr long long long ptr)
@ stdcall D3DXPlaneFromPointNormal(ptr ptr ptr)
@ stdcall D3DXPlaneFromPoints(ptr ptr ptr ptr)
@ stdcall D3DXPlaneIntersectLine(ptr ptr ptr ptr)
@ stdcall D3DXPlaneNormalize(ptr ptr)
@ stdcall D3DXPlaneTransform(ptr ptr ptr)
@ stdcall D3DXPlaneTransformArray(ptr long ptr long ptr long)
@ stdcall D3DXPreprocessShader(ptr long ptr ptr ptr ptr)
@ stdcall D3DXPreprocessShaderFromFileA(str ptr ptr ptr ptr)
@ stdcall D3DXPreprocessShaderFromFileW(wstr ptr ptr ptr ptr)
@ stdcall D3DXPreprocessShaderFromResourceA(long str ptr ptr ptr ptr)
@ stdcall D3DXPreprocessShaderFromResourceW(long wstr ptr ptr ptr ptr)
@ stdcall D3DXQuaternionBaryCentric(ptr ptr ptr ptr float float)
@ stdcall D3DXQuaternionExp(ptr ptr)
@ stdcall D3DXQuaternionInverse(ptr ptr)
@ stdcall D3DXQuaternionLn(ptr ptr)
@ stdcall D3DXQuaternionMultiply(ptr ptr ptr)
@ stdcall D3DXQuaternionNormalize(ptr ptr)
@ stdcall D3DXQuaternionRotationAxis(ptr ptr float)
@ stdcall D3DXQuaternionRotationMatrix(ptr ptr)
@ stdcall D3DXQuaternionRotationYawPitchRoll(ptr float float float)
@ stdcall D3DXQuaternionSlerp(ptr ptr ptr float)
@ stdcall D3DXQuaternionSquad(ptr ptr ptr ptr ptr float)
@ stdcall D3DXQuaternionSquadSetup(ptr ptr ptr ptr ptr ptr ptr)
@ stdcall D3DXQuaternionToAxisAngle(ptr ptr ptr)
@ stub D3DXRectPatchSize(ptr ptr ptr)
@ stub D3DXSaveMeshHierarchyToFileA(ptr long ptr ptr ptr)
@ stub D3DXSaveMeshHierarchyToFileW(ptr long ptr ptr ptr)
@ stub D3DXSaveMeshToXA(ptr ptr ptr ptr ptr long long)
@ stub D3DXSaveMeshToXW(ptr ptr ptr ptr ptr long long)
@ stub D3DXSavePRTBufferToFileA(ptr ptr)
@ stub D3DXSavePRTBufferToFileW(ptr ptr)
@ stub D3DXSavePRTCompBufferToFileA(ptr ptr)
@ stub D3DXSavePRTCompBufferToFileW(ptr ptr)
@ stdcall D3DXSaveSurfaceToFileA(ptr long ptr ptr ptr)
@ stdcall D3DXSaveSurfaceToFileInMemory(ptr long ptr ptr ptr)
@ stdcall D3DXSaveSurfaceToFileW(ptr long ptr ptr ptr)
@ stdcall D3DXSaveTextureToFileA(ptr long ptr ptr)
@ stdcall D3DXSaveTextureToFileInMemory(ptr long ptr ptr)
@ stdcall D3DXSaveTextureToFileW(ptr long ptr ptr)
@ stub D3DXSaveVolumeToFileA(ptr long ptr ptr ptr)
@ stub D3DXSaveVolumeToFileInMemory(ptr long ptr ptr ptr)
@ stub D3DXSaveVolumeToFileW(ptr long ptr ptr ptr)
@ stdcall D3DXSHAdd(ptr long ptr ptr)
@ stdcall D3DXSHDot(long ptr ptr)
@ stub D3DXSHEvalConeLight(long ptr long long long long ptr ptr ptr)
@ stdcall D3DXSHEvalDirection(ptr long ptr)
@ stdcall D3DXSHEvalDirectionalLight(long ptr float float float ptr ptr ptr)
@ stub D3DXSHEvalHemisphereLight(long ptr long long ptr ptr ptr)
@ stub D3DXSHEvalSphericalLight(long ptr long long long long ptr ptr ptr)
@ stdcall D3DXSHMultiply2(ptr ptr ptr)
@ stdcall D3DXSHMultiply3(ptr ptr ptr)
@ stdcall D3DXSHMultiply4(ptr ptr ptr)
@ stub D3DXSHMultiply5(ptr ptr ptr)
@ stub D3DXSHMultiply6(ptr ptr ptr)
@ stub D3DXSHProjectCubeMap(long ptr ptr ptr ptr)
@ stub D3DXSHPRTCompSplitMeshSC(ptr long long ptr long ptr long long ptr ptr long ptr ptr ptr ptr ptr)
@ stub D3DXSHPRTCompSuperCluster(ptr ptr long long ptr ptr)
@ stdcall D3DXSHRotate(ptr long ptr ptr)
@ stdcall D3DXSHRotateZ(ptr long float ptr)
@ stdcall D3DXSHScale(ptr long ptr float)
@ stub D3DXSimplifyMesh(ptr ptr ptr ptr long long ptr)
@ stdcall D3DXSphereBoundProbe(ptr float ptr ptr)
@ stub D3DXSplitMesh(ptr ptr long long ptr ptr ptr ptr ptr)
@ stub D3DXTessellateNPatches(ptr ptr long long ptr ptr)
@ stub D3DXTessellateRectPatch(ptr ptr ptr ptr ptr)
@ stub D3DXTessellateTriPatch(ptr ptr ptr ptr ptr)
@ stub D3DXTriPatchSize(ptr ptr ptr)
@ stub D3DXUVAtlasCreate(ptr long long long long long long ptr ptr ptr ptr long ptr long ptr ptr ptr ptr ptr)
@ stub D3DXUVAtlasPack(ptr long long long long ptr ptr long ptr long ptr)
@ stub D3DXUVAtlasPartition(ptr long long long ptr ptr ptr ptr long ptr long ptr ptr ptr ptr ptr ptr)
@ stdcall D3DXValidMesh(ptr ptr ptr)
@ stub D3DXValidPatchMesh(ptr ptr ptr ptr)
@ stdcall D3DXVec2BaryCentric(ptr ptr ptr ptr float float)
@ stdcall D3DXVec2CatmullRom(ptr ptr ptr ptr ptr float)
@ stdcall D3DXVec2Hermite(ptr ptr ptr ptr ptr float)
@ stdcall D3DXVec2Normalize(ptr ptr)
@ stdcall D3DXVec2Transform(ptr ptr ptr)
@ stdcall D3DXVec2TransformArray(ptr long ptr long ptr long)
@ stdcall D3DXVec2TransformCoord(ptr ptr ptr)
@ stdcall D3DXVec2TransformCoordArray(ptr long ptr long ptr long)
@ stdcall D3DXVec2TransformNormal(ptr ptr ptr)
@ stdcall D3DXVec2TransformNormalArray(ptr long ptr long ptr long)
@ stdcall D3DXVec3BaryCentric(ptr ptr ptr ptr float float)
@ stdcall D3DXVec3CatmullRom(ptr ptr ptr ptr ptr float)
@ stdcall D3DXVec3Hermite(ptr ptr ptr ptr ptr float)
@ stdcall D3DXVec3Normalize(ptr ptr)
@ stdcall D3DXVec3Project(ptr ptr ptr ptr ptr ptr)
@ stdcall D3DXVec3ProjectArray(ptr long ptr long ptr ptr ptr ptr long)
@ stdcall D3DXVec3Transform(ptr ptr ptr)
@ stdcall D3DXVec3TransformArray(ptr long ptr long ptr long)
@ stdcall D3DXVec3TransformCoord(ptr ptr ptr)
@ stdcall D3DXVec3TransformCoordArray(ptr long ptr long ptr long)
@ stdcall D3DXVec3TransformNormal(ptr ptr ptr)
@ stdcall D3DXVec3TransformNormalArray(ptr long ptr long ptr long)
@ stdcall D3DXVec3Unproject(ptr ptr ptr ptr ptr ptr)
@ stdcall D3DXVec3UnprojectArray(ptr long ptr long ptr ptr ptr ptr long)
@ stdcall D3DXVec4BaryCentric(ptr ptr ptr ptr float float)
@ stdcall D3DXVec4CatmullRom(ptr ptr ptr ptr ptr float)
@ stdcall D3DXVec4Cross(ptr ptr ptr ptr)
@ stdcall D3DXVec4Hermite(ptr ptr ptr ptr ptr float)
@ stdcall D3DXVec4Normalize(ptr ptr)
@ stdcall D3DXVec4Transform(ptr ptr ptr)
@ stdcall D3DXVec4TransformArray(ptr long ptr long ptr long)
@ stdcall D3DXWeldVertices(ptr long ptr ptr ptr ptr ptr)
