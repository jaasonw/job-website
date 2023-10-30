import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "$lib/components/shadcn/components/ui/accordion";
import Stats from "$lib/components/stats";
import JobsTable from "$lib/components/table";
import Updated from "$lib/components/updated";
import { UPDATE_INTERVAL } from "$lib/src/constants";

export default async function Home() {
  return (
    <section className="flex flex-col w-full max-w-7xl px-3 justify-center items-center">
      <section className="flex flex-col items-center mt-24 gap-4">
        <h1 className="text-6xl text-center font-bold">job board</h1>
        <p className="text-center text-2xl text-gray-500">need food pls hire</p>
        <Updated />
        <p className="text-gray-500 text-sm">Updated every 5 hours</p>
      </section>
      <JobsTable />
      <section className="flex flex-col items-center my-20 gap-1 w-full">
        <h2 className="text-5xl text-center font-bold">
          Frequently Asked Questions
        </h2>
        <div className="w-full">
          <Accordion type="multiple">
            <AccordionItem value="item-1">
              <AccordionTrigger>Why did you make this?</AccordionTrigger>
              <AccordionContent>
                LinkedIn, Indeed, and other job board sites all manage to have
                inaccurate filters. Searches for "entry-level" positions end up
                yielding several listings for positions requiring 5+ years of
                experience and senior level positions. We aim to build a job
                board that's actually geared towards entry level positions.
              </AccordionContent>
            </AccordionItem>
            <AccordionItem value="item-2">
              <AccordionTrigger>How do we get the data?</AccordionTrigger>
              <AccordionContent>
                We source our data from various job boards, scraping every 5
                hours and run our parsers and filters to remove all the listings
                that we just aren't interested in. Finally, the remaining jobs
                are uploaded to a Google Sheet and displayed on this website.
              </AccordionContent>
            </AccordionItem>
            <AccordionItem value="item-3">
              <AccordionTrigger>
                How do you know if a job is actually entry level?
              </AccordionTrigger>
              <AccordionContent>
                We look for key words in the job description and parse out
                details like years of experience and technical stack.
              </AccordionContent>
            </AccordionItem>
            <AccordionItem value="item-4">
              <AccordionTrigger>Why Google Sheets?</AccordionTrigger>
              <AccordionContent>
                It{" "}
                <a
                  className="underline"
                  href="https://www.levels.fyi/blog/scaling-to-millions-with-google-sheets.html"
                >
                  scales to millions
                </a>
                , it's free, and it means I won't have to host my own database.
                I see zero reasons to not to.
              </AccordionContent>
            </AccordionItem>
            <AccordionItem value="item-5">
              <AccordionTrigger>How often will this update?</AccordionTrigger>
              <AccordionContent>
                The plan is to update this every 5 hours but sometimes my cron
                job has other ideas ¯\_(ツ)_/¯
              </AccordionContent>
            </AccordionItem>
          </Accordion>
        </div>
      </section>
      <section className="my-20">
        <Stats />
      </section>
    </section>
  );
}
