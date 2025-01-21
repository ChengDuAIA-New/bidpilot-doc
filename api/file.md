# 文件接口

### 文件上传
````http request
// 上传文件
POST /api/file/upload HTTP/1.1
Content-Type: multipart/form-data;
````
````ts
Request<{
    // 文件
    file: File
    // 业务id: 根据业务类型对应不同表的主键
    businessId: string
    // 业务类型
    businessType: string
    // 业务描述
    businessDesc: string
    // 文件类型
    fileType: number
    // 文件来源: 0: 前端用户上传; 1: 后端系统上传; 2: AI系统上传
    dataFrom: number
}>
Response<{
    // 文件id
    fileId: number
    // 文件名称
    fileName: string
    // 原文件名称
    sourceName: string
    // 文件描述
    fileDesc: string
    // 文件类型
    fileType: number
    // 文件大小
    fileSize: number
}>
````
### 文件查询
````http request
// 上传文件
POST /api/file/find HTTP/1.1
Content-Type: application/json;
````
````ts
Request<{
    // 文件id
    fileId: number | null
    // 业务id: 根据业务类型对应不同表的主键
    businessId: string | null
    // 业务类型
    businessType: string | null
    // 文件类型
    fileType: number | null
}>
Response<[
    {
        // 文件id
        fileId: number
        // 文件名称
        fileName: string
        // 原文件名称
        sourceName: string
        // 文件描述
        fileDesc: string
        // 文件类型
        fileType: number
        // 文件大小
        fileSize: number
    }
]>
````
