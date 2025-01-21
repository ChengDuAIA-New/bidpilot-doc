# 流程接口

### 创建流程
````http request
POST /api/workflow/create HTTP/1.1
Content-Type: application/json;
````
````ts
Request<{
    // 项目id
    projectId: number
}>
Response<
    number
>
````

### 流程查询
````http request
POST /api/workflow/find HTTP/1.1
Content-Type: application/json;
````
````ts
Request<{
    // 项目id
    projectId: number
}>
Response<number[]>
````