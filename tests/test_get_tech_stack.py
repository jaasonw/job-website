from transform.util import get_tech_stack


def test_get_tech_stack():
    case_1 = get_tech_stack(
        """
            2+ years of experience
            2+ years of experience working with a progressive JavaScript framework such as React. 
            1+ years of experience working with TypeScript. 
            At least 6 months of experience working with any CSS framework such as tailwind, bootstrap, etc. 
            Experience testing full stack web applications
            Experience with tools surrounding web performance caching with redis/memcached, CDN rules, etc. 
            A willingness to learn new frameworks and technologies as needed
            """
    )
    assert sorted(case_1) == sorted(
        ["React", "Bootstrap", "Javascript", "Css", "Memcached", "Typescript", "Redis"]
    )
    case_2 = get_tech_stack(
        """
            Responsibilities


            Collaborate with cross-functional teams to gather and analyze requirements for new features and functionalities.
            Develop and maintain server-side applications using Java and related technologies.
            Implement data models, database schemas, and perform database operations using SQL or NoSQL databases.
            Integrate APIs, web services, and external systems into the application.
            Write clean, efficient, and maintainable code following industry best practices.
            Conduct unit testing and debugging to identify and fix issues promptly.
            Participate in code reviews to ensure code quality, performance, and maintainability.
            Stay up to date with emerging technologies, trends, and best practices in back-end development.


            Requirements


            Bachelor's degree in Computer Science, Software Engineering, or a related field.
            Strong understanding of Java programming language and object-oriented principles.
            Knowledge of back-end development concepts and frameworks, such as Spring Boot or Hibernate.
            Familiarity with databases, including SQL and/or NoSQL.
            Understanding of RESTful APIs and web services.
            Basic knowledge of version control systems, such as Git.
            Solid problem-solving and analytical skills.
            Excellent communication and collaboration abilities.
            Ability to work well in a team environment and contribute to collective goals.
            Self-motivated with a desire to learn and grow in back-end development.


            Preferred Qualifications


            Familiarity with cloud platforms, such as Amazon Web Services (AWS), Microsoft Azure, or Google Cloud Platform (GCP).
            Experience with test-driven development (TDD) and agile methodologies.
            Understanding of software development principles and practices, including code versioning, documentation, and deployment.
            """
    )
    assert sorted(case_2) == sorted(
        ["Sql", "Azure", "Git", "Nosql", "Google Cloud", "Java", "Spring", "Aws"]
    )

    case_3 = get_tech_stack(
        """
            Essential Position Responsibilities


            Develop front-end interactive experiences and back-end integrations for the company’s new Enterprise Resource Planning (ERP) system. 
            Prototype, test and iterate against designs and specification to optimize user experience and overall product performance. 
            Work with the team to strategize, architect and plan deliverables and development approaches. 
            Test and debug browsers and the company website. 
            Other duties as assigned. 


            Education And Experience


            Understanding of the web development process from start to finish required. 
            A degree in a related field is preferred. 
            1-3 years of experience preferred. 
            Experience with C# and dotnet preferred. 


            Qualifications


            Familiarity with programming languages such as HTML, CSS, JavaScript and Typescript. 
            Understanding of front end libraries/frameworks such as React and Vue. 
            Strong verbal and written communication skills. 
            Ability to troubleshoot and problem-solve independently and collaboratively. 
            Comfortable working with new technologies. 
            Knowledge of latest trends in web application development. 
            Strong attention to detail and ability to remain organized while working on multiple projects. 
        """
    )
    assert sorted(case_3) == sorted(
        ["Typescript", "C", "Javascript", "Css", "React", "Vue"]
    )
