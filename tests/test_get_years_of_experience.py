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
