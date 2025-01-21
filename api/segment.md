# 节点接口

### 节点查询
````http request
POST /api/segment/find HTTP/1.1
Content-Type: application/json;
````
````ts
Request<{
    // 项目id
    projectId: number | null
    workflowId: number | null
}>
Response<{
    workflowId : number
    segments: {
        segmentsId: number
        name: string
    }
}>
````