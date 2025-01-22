# 环节接口

### 环节查询
````http request
POST /api/segment/find HTTP/1.1
Content-Type: application/json;
````
````ts
import { ApiResponse } from '@/types/api'

Request<{
    // 项目id
    projectId: number | null
    workflowId: number | null
}>
ApiResponse<{
    workflowId : number
    segments: Array<{
        segmentsId: number
        name: string
        parentId: number
    }>
}>
````

### 下一个环节
````http request
POST /api/segment/next/{name} HTTP/1.1
Content-Type: application/json;
````
````ts
import { ApiResponse } from '@/types/api'

Request<{
    segmentsId: number
    // 下一步环节所需参数
    // ...
}>
ApiResponse<{
    segmentsId: number
    name: string
    parentId: number
}>
````
> 说明: name为环节名称，如：'上传'、'分析'、'大纲'等