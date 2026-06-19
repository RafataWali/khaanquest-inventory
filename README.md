# KhaanQuest Inventory
Internal iOS inventory and event sales management system for KhaanQuest.

## Technology Stack

- iOS: Swift and SwiftUI
- Backend: Python and FastAPI
- Database: PostgreSQL
- Database Migrations: Alembic
- Local Development: Docker
- Cloud Platform: AWS

## Project Structure

```text
ios/                 Native iOS application
backend/             FastAPI backend
database/            Database migrations and seed data
infrastructure/      Docker and AWS infrastructure
docs/                Product and technical documentation
.github/workflows/   CI workflows

## Technology Selection and Trade-offs

## 技术选型与取舍

### 中文

本项目的技术选型以业务需求、长期维护、离线能力、数据一致性、开发效率和未来扩展性为主要判断标准，而不是单纯选择最流行或最新的技术。

#### 1. iOS：Swift + SwiftUI + Xcode

选择原生 SwiftUI，是因为本项目当前只面向 iPhone，并且需要较好的离线存储、系统权限、相机、扫码、通知和设备性能支持。SwiftUI 是 Apple 官方 UI 框架，能够直接使用 iOS 原生能力，并减少跨平台适配问题。

暂时不选择 React Native 或 Flutter，是因为它们更适合同时开发 iOS 和 Android。KhaanQuest 现阶段没有 Android 需求，引入跨平台框架会增加额外依赖、桥接层和调试复杂度。暂时不选择 UIKit，是因为 SwiftUI 更适合新项目，代码量更少，界面开发速度更快；后续如遇到 SwiftUI 无法满足的复杂功能，可以局部结合 UIKit。

#### 2. 后端：Python 3.13 + FastAPI

选择 Python，是因为开发效率高、代码易读，并且拥有成熟的数据分析、自动化、AI 和云服务生态，符合本项目未来可能增加销量分析、库存预测和 AI 功能的方向。

选择 FastAPI，是因为它结构轻量、性能较好、支持异步请求、类型校验，并可以根据代码自动生成 OpenAPI 文档，适合构建前后端分离的移动应用 API。

暂时不选择 Django，是因为 Django 自带完整的模板、后台管理和传统网站功能，而本项目主要需要 API，使用 Django 会引入部分暂时不需要的功能。暂时不选择 Node.js，是因为虽然 Node.js 也适合 API 开发，但本项目未来计划加强数据分析、自动化和 AI 能力，Python 的整体生态更加统一。暂时不选择 Java Spring Boot，是因为它更适合大型企业团队和复杂微服务系统，但初期开发成本、配置复杂度和代码量相对更高，不适合当前小团队快速验证产品。

#### 3. Python 版本：3.13

选择 Python 3.13，是因为它是较新的稳定版本，同时核心后端依赖的兼容性相对成熟。项目更重视稳定、可复现和减少环境问题，而不是第一时间使用最新的大版本。

暂时不选择 Python 3.14，是因为新大版本发布初期，部分第三方数据库、迁移、测试或部署工具可能还没有完成充分验证。等核心依赖和生产环境支持更加成熟后，可以再评估升级。

#### 4. 数据库：PostgreSQL

选择 PostgreSQL，是因为库存系统涉及商品、仓库、调拨、销售、盘点和库存流水，这些数据之间存在明确关系，并且需要事务、约束和较强的数据一致性。PostgreSQL 对关系型数据、事务处理、复杂查询、JSON 数据和并发控制都有较好的支持。

暂时不选择 MongoDB，是因为库存数据不是以灵活文档结构为主，而是需要严格关系和一致性，使用文档数据库会增加数据约束和关联查询的管理成本。暂时不选择 SQLite 作为中央数据库，是因为 SQLite 更适合单机本地存储，不适合多个用户和多个地点共享库存；但 SQLite 或 SwiftData 可以继续用于 iOS 离线缓存。MySQL 也可以完成大部分需求，但 PostgreSQL 在复杂查询、数据约束、JSON 支持和未来分析能力方面更符合本项目方向。

#### 5. 本地离线存储：SwiftData

选择 SwiftData，是因为它是 Apple 原生的数据持久化方案，能够与 SwiftUI 较自然地结合，适合保存本地商品、库存快照、待同步销售记录和离线操作队列。

暂时不直接使用第三方移动数据库，是为了减少外部依赖和维护成本。Core Data 功能成熟，但 SwiftData 的开发方式更现代、代码更简洁。后续如出现复杂同步、跨平台或大规模本地数据需求，可以重新评估 Realm 或其他方案。

#### 6. 本地服务环境：Docker

选择 Docker，是为了用统一方式运行 PostgreSQL 和其他后台服务，避免每台电脑单独安装和配置数据库。通过 Docker Compose，可以用一条命令启动固定版本的数据库、网络和持久化存储，使开发环境更容易复现。

暂时不直接在 macOS 中安装 PostgreSQL，是因为本地安装容易产生版本冲突、路径问题和配置差异。暂时不把 FastAPI 也完全放进 Docker，是因为开发早期直接在本机虚拟环境运行 Python，代码修改和调试更方便；等后端结构稳定后，再增加完整的应用容器。

#### 7. 版本控制：Git + GitHub

选择 Git，是因为它可以记录每次代码变化、创建分支、回退错误和合并不同开发内容。选择 GitHub，是因为它同时提供远程备份、Pull Request、Issue、代码审查和 GitHub Actions，适合未来团队协作和自动测试。

暂时不选择 GitLab 或 Bitbucket，并不是因为它们能力不足，而是 GitHub 的生态、学习资源、第三方集成和个人开发体验更适合当前项目。未来如果公司有内部部署或特定合规要求，可以迁移到其他平台。

#### 8. 云平台：AWS

选择 AWS，是因为它可以提供 RDS PostgreSQL、对象存储 S3、后端托管、监控、备份和权限管理，能够覆盖本项目未来从测试到生产的主要需求。AWS 的服务组合完整，也便于后续学习云架构和基础设施管理。

暂时不选择 Azure，是因为当前项目并不依赖 Microsoft 企业生态、Active Directory 或 .NET。暂时不选择 Google Cloud，是因为虽然其数据和 AI 服务具有优势，但本项目当前更需要成熟的关系型数据库、存储和通用后端部署能力。三者都可以实现本项目，AWS 是当前基于项目需求和个人学习方向做出的统一选择。

#### 9. 架构方式：原生 iOS + REST API + 关系型数据库

选择前后端分离，是为了让 iOS App、后端业务规则和数据库职责清晰。iOS 负责界面、离线操作和用户交互；FastAPI 负责权限、库存规则、同步逻辑和业务校验；PostgreSQL 负责可靠保存数据。

暂时不采用微服务架构，是因为当前系统规模和团队人数还不需要多个独立服务。过早拆分微服务会增加部署、日志、网络、认证和数据一致性成本。初期采用结构清晰的模块化单体，未来当用户量、团队规模或业务复杂度增长后，再根据实际瓶颈拆分服务。

---

### English

The technology stack is selected according to business requirements, maintainability, offline capability, data consistency, development speed, and future scalability rather than simply choosing the newest or most popular technologies.

#### 1. iOS: Swift, SwiftUI, and Xcode

SwiftUI is selected because the application currently targets iPhone only and requires reliable access to native features such as offline storage, camera access, barcode scanning, notifications, permissions, and device performance. As Apple’s official UI framework, SwiftUI provides direct integration with the iOS platform and reduces cross-platform compatibility issues.

React Native and Flutter are not selected at this stage because they are most valuable when both iOS and Android must be supported. KhaanQuest currently has no Android requirement, so adding a cross-platform runtime, bridge layer, and additional dependencies would create unnecessary complexity. UIKit is not the primary choice because SwiftUI provides a more modern development model and requires less code for a new application, although UIKit can still be used for specific features when necessary.

#### 2. Backend: Python 3.13 and FastAPI

Python is selected because it supports rapid development, readable code, automation, data analysis, AI, and cloud integration. This also aligns with possible future features such as sales analytics, inventory forecasting, and AI-assisted operations.

FastAPI is selected because it is lightweight, supports asynchronous requests, provides type validation, and automatically generates OpenAPI documentation. It is well suited to a mobile application that communicates with a separate backend API.

Django is not selected because it includes a complete website framework, template engine, and administration features that are not currently required for an API-focused mobile system. Node.js is a valid alternative, but Python provides a more unified path for future analytics, automation, and AI features. Java Spring Boot is not selected because its configuration, development overhead, and code volume are less suitable for a small team building and validating the first version of the product.

#### 3. Python Version: 3.13

Python 3.13 is selected because it is a recent stable version with relatively mature compatibility across the planned backend dependencies. The project prioritises stability and reproducibility over immediately adopting the latest major release.

Python 3.14 is not selected initially because some database, migration, testing, or deployment packages may require additional time to complete full compatibility testing. An upgrade can be evaluated later when the complete dependency stack is proven stable.

#### 4. Database: PostgreSQL

PostgreSQL is selected because inventory management involves strongly related data such as products, locations, transfers, sales, stock counts, and inventory movements. These operations require transactions, constraints, concurrency control, and reliable data consistency. PostgreSQL also provides strong support for relational queries, JSON data, reporting, and future analytics.

MongoDB is not selected because the primary data model requires strict relationships and consistency rather than flexible document structures. SQLite is not suitable as the central shared database because it is designed mainly for local or single-device use, although SQLite or SwiftData may still be used for offline storage on the iPhone. MySQL could support most of the requirements, but PostgreSQL provides a stronger fit for complex queries, constraints, JSON support, and future analytical workloads.

#### 5. Local Offline Storage: SwiftData

SwiftData is selected because it is Apple’s native persistence framework and integrates naturally with SwiftUI. It is suitable for storing product data, inventory snapshots, pending sales, and offline synchronisation queues on the device.

A third-party mobile database is not selected initially in order to reduce external dependencies and maintenance requirements. Core Data is mature, but SwiftData offers a more modern and concise development model. Realm or another solution can be reconsidered if future requirements include highly complex synchronisation, cross-platform support, or significantly larger local datasets.

#### 6. Local Services: Docker

Docker is selected to run PostgreSQL and supporting services in a consistent and repeatable environment. Docker Compose can define the database version, network, ports, and persistent storage so that the same environment can be recreated on another development machine.

A direct PostgreSQL installation on macOS is not preferred because it can create version conflicts, path issues, and configuration differences between developers. FastAPI is not fully containerised during the earliest development stage because running Python directly inside a virtual environment provides a faster editing and debugging workflow. The backend application can be containerised after the project structure becomes stable.

#### 7. Version Control: Git and GitHub

Git is selected to record changes, support branches, recover previous versions, and merge work safely. GitHub is selected because it provides remote backup, pull requests, issue tracking, code review, and GitHub Actions for future automated testing and deployment.

GitLab and Bitbucket are not rejected because of technical limitations; they could also support this project. GitHub is selected because its ecosystem, documentation, integrations, and developer experience are more suitable for the current project. Migration remains possible if future organisational or compliance requirements change.

#### 8. Cloud Platform: AWS

AWS is selected because it can provide RDS PostgreSQL, S3 object storage, backend hosting, monitoring, backups, networking, and access control within one cloud platform. It supports the expected path from development to production and also aligns with the project’s cloud infrastructure learning goals.

Azure is not selected because the project does not currently depend on the Microsoft enterprise ecosystem, Active Directory, or .NET. Google Cloud is not selected because, although it offers strong data and AI services, the current requirements are more focused on general backend hosting, relational databases, and object storage. All three major cloud providers could support the system; AWS is the selected platform for consistency and alignment with the current project direction.

#### 9. Architecture: Native iOS, REST API, and Relational Database

A separated client-server architecture is selected so that responsibilities remain clear. The iOS application handles the interface, offline actions, and user interaction. FastAPI handles permissions, inventory rules, synchronisation, and business validation. PostgreSQL provides reliable shared data storage.

A microservices architecture is not selected at the beginning because the current product size and team structure do not require multiple independently deployed services. Introducing microservices too early would add unnecessary complexity in deployment, networking, authentication, logging, monitoring, and data consistency. The project will begin as a modular monolith and services can be separated later when real scaling or organisational requirements justify the additional complexity.
