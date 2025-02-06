# 项目接口

### 创建项目
````http request
POST /api/project/create HTTP/1.1
Content-Type: application/json;
````
````ts
import { ApiResponse } from '@/types/api'

Request<{
    // 项目名称
    name: string
    // 项目编号
    number: string
    // 项目类型
    type: string
    // 招标单位
    orgName: string
    // 发布时间
    releaseDate: Date
    // 项目描述
    description: string | null
}>
ApiResponse<
    {
        // 项目id
        id: number
        // 项目名称
        name: string
        // 项目编号
        number: string
        // 项目类型
        type: string
        // 招标单位
        orgName: string
        // 发布时间
        releaseDate: Date
        // 项目描述
        description: string | null
    }
>
````

### 项目查询
````http request
POST /api/project/find HTTP/1.1
Content-Type: application/json;
````
````ts
import { ApiResponse } from '@/types/api'

Request<{
    // 项目Id
    id: number | null
    // 项目名称
    name: string | null
    // 项目编号
    number: string | null
    page?: number
    size?: number
    sort?: string
}>
ApiResponse<PageResponse<{
    // 项目id
    id: number
    // 项目名称
    name: string
    // 项目编号
    number: string
    // 项目类型
    type: string
    // 招标单位
    orgName: string
    // 发布时间
    releaseDate: Date
    // 项目描述
    description: string | null
}>>
````