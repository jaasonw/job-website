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
