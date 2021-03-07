---
id: GSoC-All-Final-Reports
title: GSoC All Final Reports
---

## Bismita Guha - GSoC'20
### About the Project

Open Source Programs (OSP) is an [original project](https://summerofcode.withgoogle.com/archive/2020/organizations/5270382996619264/) which I proposed to [AnitaB.org Open Source](https://github.com/anitab-org) during GSoC'20. The purpose of this project was to simplify the management work of the mentors and organizations. The goal is to make reviewing and notifying simpler, systematic and manageable. This will help in easy processing and hosting of applications and forms. The following features were to be covered during GSoC as a part of the MVP:

- Building a Minimal Viable Product (MVP) as the first version of the application.
- Digitalize student progress tracking
- Automated updating of Progress Sheets along with the feature of manual editing
- Complete APIs with CRUD views
- Add Frontend to support APIs
- Add relevant documentation and tests for the same.

[Backend Repo](https://github.com/anitab-org/open-source-programs-backend) [Frontend Repo](https://github.com/anitab-org/open-source-programs-web)

### Documentation

- [Backend Documentation](https://osp-backend-docs.surge.sh/)
- [Frontend Documentation](http://osp-web-docs.surge.sh/)
- [API docs](https://documenter.getpostman.com/view/11324046/Szzoaw1q)

### Team

- Student: [Bismita Guha](https://github.com/bismitaguha)
- Mentors: [Abha Wadjikar](https://github.com/abha224), [Siddharth Venu](https://github.com/sidvenu) & [Monal Shadi](https://github.com/Monal5031)
- Admin: [Maybelline Burgos](https://github.com/mayburgos)

### Tech Stack
	
| Backend 	     | Django, Django REST Framework |
| Frontend 	     | ReactJS, Redux                |
| Database 	     | PostgreSQL                    |
| API docs & Testing | Postman-Newman                |

### Blogs & Wiki

During the GSoC period, I penned down my experiences through Medium Blogs. They contain summary of my work in the project, and also some extra information.

- Personal Wiki - [Bismita Guha-GSoC'20](https://osp-backend-docs.surge.sh/docs/2020-Bismita-Guha)
- Intro Blog - [Intro to GSoC’20 with AnitaB.org Open Source](https://medium.com/anitab-org-open-source/intro-to-gsoc20-with-anitab-org-open-source-966df7922210)
- Week 1 - [API testing using Postman and Newman](https://medium.com/anitab-org-open-source/gsoc20-coding-phase-week-1-4f0df051fdf1
)
- Week 2 - [JWT Authentication using Django REST Framework](https://medium.com/anitab-org-open-source/gsoc20-coding-phase-week-2-6d13932e372f)
- Week 3 - [Email confirmation process using Django and Sendgrid](https://medium.com/anitab-org-open-source/gsoc20-coding-phase-week-3-9d084ea55bdc
)
- Week 4 - [Form validations in ReactJS](https://medium.com/anitab-org-open-source/form-validations-in-reactjs-4838ce32bd83)
- Week 5 - [Working with multiple serializers](https://medium.com/anitab-org-open-source/working-with-multiple-serializers-76858c07e50d)
- Week 6 - [Redux state management for different request methods](https://medium.com/anitab-org-open-source/redux-state-management-for-different-request-methods-fc1f29a82d3a)
- Week 7 - [More into Redux…](https://medium.com/anitab-org-open-source/more-into-redux-e0b1f8e26867)
- Week 8 - [Experimenting with Django](https://medium.com/anitab-org-open-source/experimenting-with-django-f5bc4d563996)
- Week 9 - [Why prefer Server-Side Rendering?)](https://medium.com/anitab-org-open-source/why-prefer-server-side-rendering-157b4ad41e45)
- Week 10 - [Uploading files to AWS using ReactJS](https://medium.com/anitab-org-open-source/uploading-files-to-aws-using-reactjs-9f3f85c0135d)
- Week 11 - [Why contribute to Open Source?](https://medium.com/anitab-org-open-source/why-contribute-to-open-source-af5bc966e295)
- Week 12 - [Winding up GSoC’20](https://medium.com/anitab-org-open-source/winding-up-gsoc20-89203bbf85e4)

### Contributions during GSoC
- [Frontend PRs from June 1, 2020 - August 31, 2020](https://github.com/anitab-org/open-source-programs-web/pulls?q=is%3Apr+author%3Abismitaguha+created%3A%3E2020-06-01+created%3A%3C2020-08-31)
- [Backend PRs from June 1, 2020 - August 31, 2020](https://github.com/anitab-org/open-source-programs-backend/pulls?q=is%3Apr+author%3Abismitaguha+created%3A%3E2020-06-01+created%3A%3C2020-08-31)

### Important Contributions
### Frontend Repo
| #PR     | Feature Integrated                                      |
|---------|---------------------------------------------------------|
| [#18](https://github.com/anitab-org/open-source-programs-web/pull/18) | Project Setup using create-react-app |
| [#27](https://github.com/anitab-org/open-source-programs-web/pull/27) | User Registration |
| [#28](https://github.com/anitab-org/open-source-programs-web/pull/28) | User Login |
| [#35](https://github.com/anitab-org/open-source-programs-web/pull/35) | Filling and editing of User Information |
| [#39](https://github.com/anitab-org/open-source-programs-web/pull/39) | Creating, editing and deletion of forms and form fields |
| [#42](https://github.com/anitab-org/open-source-programs-web/pull/42) | Uploading files to AWS S3 bucket using ReactJS |
| [#48](https://github.com/anitab-org/open-source-programs-web/pull/48) | Filling and editing of form responses |
| [#54](https://github.com/anitab-org/open-source-programs-web/pull/54) | Feature for viewing and searching in form submissions |
| [#51](https://github.com/anitab-org/open-source-programs-web/pull/51) | Viewing and refreshing of Zulip Stats |

### Backend Repo
| #PR     | Feature Integrated                                                 |
|---------|--------------------------------------------------------------------|
| [#6](https://github.com/anitab-org/open-source-programs-backend/pull/6)  | Project Setup with Django |
| [#19](https://github.com/anitab-org/open-source-programs-backend/pull/19) | Registration API |
| [#22](https://github.com/anitab-org/open-source-programs-backend/pull/22) | Login API and send email feature |
| [#28](https://github.com/anitab-org/open-source-programs-backend/pull/28) | CRUD operations for form and field APIs |
| [#31](https://github.com/anitab-org/open-source-programs-backend/pull/31) | Creating and editing of form responses |
| [#36](https://github.com/anitab-org/open-source-programs-backend/pull/36) | Feature to search submissions list and viewing of user profile |
| [#37](https://github.com/anitab-org/open-source-programs-backend/pull/37) | Feature to view and update Zulip Stats |

### Work left to do

- **Github integration to retrieve stats of a user** - Currently Zulip Stats of a specific user can be viewed by admins and the logged-in user. Similarly, Viewing of GitHub Stats simplifies the processing of the application for the Admins.

- **Deployment of the application** - The application has to be deployed to AWS, but there are currently problems with the permissions. Also, the application needs to be renamed because, over the development process, it has been made more flexible than was originally planned. So once finalized, the application will be deployed.

### Future Scope of application
| Idea                                                  | Description                                                                                                                                                                                                         |
|-------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cross-platform app                   | Create an app functional on devices with different operating systems. You may use Flutter or React-Native                        |
| Tags                    | An option to create tags on forms and be able to search by tags    |
| Notifications                    | Notify the user on getting accepted, rejected or waitlisted    |
| Approval of Admins               | Feature to add approval whenever anyone signs-up as an admin, because we cannot allow admin access across the app to everyone   |
| Email on Acceptance        | Whenever the acceptance status of a student gets updated they receive an email, mentioning the change.  |

### Challenges Faced

- **Email send feature** - faced challenges integrating with the application, especially due to understanding the documentation and purpose of variables.
- **Uploading to AWS** - Had no knowledge of setting up AWS buckets or keys. So watched tutorials on setup and faced problems on integrating with ReactJS. There was no documentation on integration with ReactJS, so it took time finding solutions to the errors arising and finishing this PR.
- **Errors in React state updates** - Faced a bug while handling states in one PR, which took around 1 week to get solved but were usually basic code changes.
- **Github API** - Github APIs have limits and that is creating problems currently in the project while testing my code.
- **Code quality** - Before the start of the GSoC period I wasn’t aware much about JS coding guidelines, so that would cause delays on the PRs.
 - **Time management** - During the last phase, my college internship season and classes were ongoing, which became a problem as I had to switch between working and multitask at times.

### Takeaways

Overall, GSoC'20 has been a wonderful experience for me. I learned specifically about the importance of Documentation and maintaining consistent code quality. I became proficient in handling errors, debugging, and completing with minimum delay. Also, this was my first experience at writing frontend code and working with Redux. As a person I would say, handling multiple branches on my local, Google Sheets & Docs and working with a varied number of sources has made me more organized. I would say Open Source provides a wonderful learning platform for aspiring developers. I would continue to participate in more such programs after this wonderful experience.
