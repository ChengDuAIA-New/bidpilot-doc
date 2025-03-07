# 流程接口

### 创建流程
````http request
POST /api/workflow/create HTTP/1.1
Content-Type: application/json;
````
````ts
import { ApiResponse } from '@/types/api'

Request<{
    // 项目id
    projectId: number
}>
ApiResponse<
    number
>
````

### 流程查询
````http request
POST /api/workflow/find HTTP/1.1
Content-Type: application/json;
````
````ts
import { ApiResponse } from '@/types/api'

Request<{
    // 项目id
    projectId: number
}>
ApiResponse<{
    workflowId: number
    projectId: number
    status: string
    createTime: string
    currentSegmentId: number
}[]>
````