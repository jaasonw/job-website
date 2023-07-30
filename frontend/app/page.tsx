import JobsTable from "$lib/components/table";
import Updated from "$lib/components/updated";
import { UPDATE_INTERVAL } from "$lib/src/constants";

export default function Home() {
  return (
    <section className="flex flex-col w-full max-w-7xl px-3 justify-center items-center">
      <section className="flex flex-col items-center mt-24 gap-4">
        <h1 className="text-6xl text-center font-bold">
          No BS SWE Jobs for College Kids and mfs who graduated from Student to
          Unemployed
        </h1>
        <p className="text-center text-2xl text-gray-500">
          We'll sift through all the BS so you don't have to
        </p>
        <Updated />
        <p className="text-gray-500 text-sm">Updated every 5 hours</p>
      </section>
      <JobsTable />
      <section className="flex flex-col items-center my-52 gap-1">
        <h2 className="text-5xl text-center font-bold">
          So what does this mean for you?
        </h2>
        <div className="flex flex-col text-center text-xl gap-3">
          <span>❌ No Linkedin "Promoted" BS</span>
          <span>❌ No Senior Developer position BS</span>
          <span>
            ❌ No "Entry Level" positions with 5-7 years of experience BS
          </span>
          <span>❌ No Security Clearance BS</span>
          <span>❌ No Jobot, Cybercoders etc. recruiting agency BS</span>
        </div>
      </section>
      <section className="flex flex-col items-center my-20 gap-1">
        <h2 className="text-5xl text-center font-bold">FAQ</h2>
        <div className="grid md:grid-cols-2 text-left gap-4 mt-5">
          <div>
            <h3 className="text-xl font-bold">Why did you make this?</h3>
            <p className="text-lg">
              LinkedIn, Indeed, and other job board sites all manage to have
              inaccurate filters. Searches for "entry-level" positions end up
              yielding several listings for positions requiring 5+ years of
              experience and senior level positions. This site aims to fix that
              by automatically filtering and curating job listings for new
              grads.
            </p>
          </div>
          <div>
            <h3 className="text-xl font-bold">How does this work?</h3>
            <p className="text-lg">
              First, we scrape the job postings from various job boards. Then,
              we run our filters on it to remove all the listings that we just
              aren't interested in. Finally, the remaining jobs are uploaded to
              a Google Sheet and displayed on this website.
            </p>
          </div>
          <div>
            <h3 className="text-xl font-bold">
              How do you know if a job is suitable for new grads?
            </h3>
            <p className="text-lg">
              We use advanced artificial intelligence and language models to-
              Nah I'm just kidding, just a simple regex and keyword search. For
              instance, if a job listing contains the word "senior", we can just
              throw it out. Additionally, we parse out the years of experience
              from the job description and throw out anything asking for more
              than 3 years.
            </p>
          </div>
          <div>
            <h3 className="text-xl font-bold">
              What recruiting agencies are filtered out?
            </h3>
            <p className="text-lg">
              See:{" "}
              <a
                className="underline"
                href="https://github.com/jaasonw/sweify/blob/main/src/transform/__init__.py#L37"
              >
                here
              </a>
              . If you think I missed any, feel free to open a PR or shoot me an
              issue{" "}
              <a
                className="underline"
                href="https://github.com/jaasonw/sweify/issues"
              >
                here
              </a>
              .
            </p>
          </div>
          <div>
            <h3 className="text-xl font-bold">Why Google Sheets?</h3>
            <p className="text-lg">
              So it can{" "}
              <a
                className="underline"
                href="https://www.levels.fyi/blog/scaling-to-millions-with-google-sheets.html"
              >
                scale to millions
              </a>
              . Also because it's free and it means I won't have to host my own
              database
            </p>
          </div>
          <div>
            <h3 className="text-xl font-bold">How often will this update?</h3>
            <p className="text-lg">
              The plan is to update this every 5 hours but sometimes my cron job
              has different ideas ¯\_(ツ)_/¯
            </p>
          </div>
        </div>
      </section>
    </section>
  );
}
