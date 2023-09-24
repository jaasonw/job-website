from transform.util import get_years_of_experience


def test_get_years_of_experience():
    assert (
        get_years_of_experience(
            """
            5+ years of professional software development experience
            Proficiency in one or more programming languages and frontend frameworks, 
            especially Typescript/Javascript/React. 
            Strong CS fundamentals and experience with web technologies (HTML/JS/CSS) 
            and REST APIs
            Self aware of strengths and seeking to constantly learn and improve
            Strong written and verbal communication
            """
        )
        == 5
    )
    assert (
        get_years_of_experience(
            """
            Bachelor of Science in Computer Science, Computer Information Systems or 
            equivalent experience required
            2-4 years of software development experience required 
            Demonstrated, progressive experience working with JavaScript frameworks
            Prior experience with PHP frameworks, such as Laravel or others
            Proven ability to write clean, clear and commented code 
            """
        )
        == 3
    )
    assert (
        get_years_of_experience(
            """
            Requires a Masters degree in Information Systems, or related field 
            or equivalent, and two (2) years of experience producing and 
            integrating frameworks to support development across various 
            platforms and teams. Prior experience must include (2) years of 
            experience developing mobile applications using modern Agile 
            techniques including Scrum; collaborating with UI designers and 
            product managers to break down requirements into work packages and 
            craft compelling mobile user experiences; designing and developing 
            reusable cross-platform UI components; applying architectural design 
            patterns including MVC; measuring, identifying and resolving performance 
            bottlenecks
            """
        )
        == 2
    )
    assert (
        get_years_of_experience(
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
        == 2
    )
    assert (
        get_years_of_experience(
            """
            
         As a Software Engineer with the Commerce Engineering (part of Cisco IT), you will develop scalable futuristic solutions to address new business models, business challenges and help drive digital transformation. You will collaborate on multi-functional projects to identify areas for improvement. You will analyze internal processes, data, and problems, and identify benefits from enabling new capabilities by using new & emerging digital and cloud technologies. You will: Deliver scalable multi cloud solutions Develop simple solutions to address complex problems Implement new features in a highly collaborative environment with product managers, UI/UX specialists, and software & hardware engineers. Work closely with Scrum Leads, Product owner and global delivery teams to drive and be a key contributor to Project releases and sprint payloads. Collaborate cross-functionally with other IT teams to implement an integrated digital experience. Who You'll Work With 1. You'll work with business partners as well as your team of data and IT professionals, scrum teams, and other business analysts. You'll get to work with leaders in the industry to shape the future of Cisco's customer and partner lifecycle. 2. You will work in the Cisco Commerce Engineering and Solution teams managing feature development for Cisco Commerce. 3. You will work with Product Owners for managing backlog and deciding effective delivery methods 4. You will be working with Cross Functional teams to build features for end-to-end Commerce processes Job Responsibilities Develop high-quality software design and architecture for building customized solutions to support critical business functions and meet project objectives, client requirements and company goals Document and demonstrate solutions by developing documentation, charts, code comments. Support and develop software engineers by providing advice, coaching, peer reviews. Develop tools and applications by producing clean, efficient code, participate in technical reviews, peer reviews for the design, code, and end -to-end application development of one or more components. Communicate and collaborate with project managers, clients and other developers to design cohesive project strategies throughout all phases of development, testing and deployment Maintain a flexible and proactive work environment to facilitate a quick response to changing project requirements and customer objectives, and innovate ways to meet mission goals successfully Interact directly with clients, managers and end users as necessary to analyze project objectives and capability requirements, including specifications for user interfaces, customized applications and interactions with internal Salesforce instances Be a persistent, creative problem solver Job Skills & Qualifications Required skills : · BS or MS degree in Computer Science or related elds 7+ years of experience in software development Self-motivated and creative Excellent knowledge on Java/J2EE stack, Network modelling, Proficient with Java / J2EE stack, Microservices architecture, OOPS, Data structures and algorithms , Databases like Oracle, Cassandra, MongoDB, Object- oriented Programming , Multithreading, frameworks like Spring boot, JPA, JUnit, Mocking Frameworks & Akka is a plus. · Experience with real time messaging systems like Kafka, RabbitMQ Experience in developing secure, highly scalable distributed platforms and micro services. Extensive knowledge of Secure RESTful API design, JSON, Proto-Buf and good understanding of Authentication and Authorization concepts. · Strong debugging and performance tuning. Evaluate open-source components for potential use in the platform. Experience with Git, CI, and deployment tools. Proven track record leveraging industry best practices and standards, Agile Methodologies and DevOps. #WeAreCisco, where each person is unique, but we bring our talents to work as a team and make a difference powering an inclusive future for all. We embrace digital, and help our customers implement change in their digital businesses. Some may think we're "old" (36 years strong) and only about hardware, but we're also a software company. And a security company. We even invented an intuitive network that adapts, predicts, learns, and protects. No other company can do what we do - you can't put us in a box! But "Digital Transformation" is an empty buzz phrase without a culture that allows for innovation, creativity, and yes, even failure (if you learn from it.) Day to day, we focus on the give and take. We give our best, give our egos a break, and give of ourselves (because giving back is built into our DNA.) We take accountability, bold steps, and take difference to heart. Because without diversity of thought and a dedication to equality for all, there is no moving forward. So, you have colorful hair? Don't care. Tattoos? Show o# your ink. Like polka dots? That's cool. Pop culture geek? Many of us are. Passion for technology and world changing? Be you, with us! 
      
            """
        )
        == 7
    )
    assert (
        get_years_of_experience(
            """
            Software Engineer (Full-Stack/Mobile) Remote (US Only) San 
            Francisco, California $120k $200k +  up to 0.50% Our Client: Our 
            client is the market-leading credit card scanner that works on all 
            credit cards. With our fast and easy integration, businesses can 
            boost payment conversion by over 5%, and reduce fraud by over 50% 
            with only an hour of engineering work. We are available as a mobile 
            SDK as well as a web API. What they do: Our client is building the 
            future of authentication, starting with the ability to make 
            seamless, fraud-free payments on any mobile device. Our first 
            product is an SDK that, by imaging a credit card, supports apps 
            in preventing fraud and enhancing conversion. The SDK is powered by 
            a deep learning model tailored for device execution. We'd love to 
            hear from you if you wish to be a part of one of the first 
            organisations working in the deep learning on mobile industry! Role 
            Summary: We're looking for a Software Engineer (Full-Stack) to join 
            Our Client as part of the founding engineering team. You will 
            work directly with the CEO to design and build new features, roll 
            out new products, and increase customer yield and retention. You 
            will be expected to ship fast, iterate rapidly, and identify 
            ongoing opportunities to deliver value to customers. 5 - 12 years 
            of relevant work experience. However, there are always exceptions 
            to the rule if the candidate is exceptional in other ways. Has 
            experience with writing, releasing, maintaining at least one of: 
            mobile code, backend code, or computer vision models (and is 
            interested in learning the rest) 2+ years relevant experience at a 
            reputable startup is a MUST Expertise in either iOS or Android 
            Professional experience & expertise in Swift and/or Java Ideal 
            candidate traits Accustomed to having significant ownership over 
            user-facing product Has strong, demonstrable experience shipping 
            high-quality products Is comfortable in a variety of engineering 
            settings, from frontend UX changes to database design to 
            quick-and-dirty python scripts Likes to ship code and test 
            user-facing changes Can work independently Has experience with 
            writing, releasing, maintaining at least one of: mobile code, 
            backend code, or computer vision models (and is interested in 
            learning the rest) Ideally has expertise in Swift or Java About 
            The Team We leverage our expertise in customer experience, fraud 
            prevention, and computer vision to build products that delight our 
            customers. Our mission-critical challenge? Reducing fraud and 
            improving conversion for our customers.
            """
        )
        == 12
    )
