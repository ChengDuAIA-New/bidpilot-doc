# 项目接口

### 创建项目
````http request
POST /api/project/create HTTP/1.1
Content-Type: application/json;
````
````ts
Request<{
    // 项目名称
    projectName: string
    // 项目编号
    projectNumber: string
    // 项目类型
    projectType: string
    // 招标单位
    orgName: string
    // 发布时间
    releaseDate: Date
    // 项目描述
    projectDesc: string | null
}>
Response<
    {
        // 项目id
        projectId: number
        // 项目名称
        projectName: string
        // 项目编号
        projectNumber: string
        // 项目类型
        projectType: string
        // 招标单位
        orgName: string
        // 发布时间
        releaseDate: Date
        // 项目描述
        projectDesc: string | null
    }
>
````

### 项目查询
````http request
POST /api/project/find HTTP/1.1
Content-Type: application/json;
````
````ts
Request<{
    // 项目Id
    projectId: number | null
}>
Response<[
    {
        // 项目id
        projectId: number
        // 项目名称
        projectName: string
        // 项目编号
        projectNumber: string
        // 项目类型
        projectType: string
        // 招标单位
        orgName: string
        // 发布时间
        releaseDate: Date
        // 项目描述
        projectDesc: string | null
    }
]>
````