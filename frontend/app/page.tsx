import JobsTable from "$lib/components/table";
import Updated from "$lib/components/updated";
import { UPDATE_INTERVAL } from "$lib/src/constants";

export default function Home() {
  return (
    <section className="flex flex-col w-full justify-center items-center ">
      <section className="flex flex-col items-center max-w-6xl my-36 gap-4 h-screen">
        <h1 className="text-6xl text-center font-bold">
          No BS SWE Jobs for College Kids and mfs who graduated from Student to
          Unemployed
        </h1>
        <p className="text-center text-2xl text-gray-500">
          We'll sift through all the BS so you don't have to
        </p>
        <Updated></Updated>
        <p className="text-gray-500 text-sm">
          Updated every {UPDATE_INTERVAL / 60 / 60} hours
        </p>
        <JobsTable></JobsTable>
      </section>
      <section className="flex flex-col items-center max-w-6xl my-20 gap-1">
        <h2 className="text-5xl text-center font-bold">
          So what does this mean for you?
        </h2>
        <p className="text-center text-2xl">Great question, This means</p>
        <p className="text-center text-2xl">❌ No Linkedin "Promoted" BS</p>
        <p className="text-center text-2xl">
          ❌ No Senior Developer position BS
        </p>
        <p className="text-center text-2xl">
          ❌ No "Entry Level" positions with 5-7 years of experience BS
        </p>
        <p className="text-center text-2xl">❌ No Security Clearance BS</p>
        <p className="text-center text-2xl">
          ❌ No Jobot, Cybercoders, etc. recruiting agency BS
        </p>
      </section>
      <footer className="flex flex-col text-xs w-full p-4 items-center text-white bg-black">
        <span>
          Disclaimer: All the jobs displayed on this website are collected from
          different public sources. We don&apos;t have any partnership or gain
          with the companies.
        </span>
        <span>
          If I helped your job search in any way,{" "}
          <a href="https://jason-wong.me/donate" className="underline">
            consider funding my boba addiction
          </a>
        </span>
        <span>
          © 2023 | Made by{" "}
          <a href="https://jason-wong.me/" className="underline">
            Jason Wong
          </a>
        </span>
      </footer>
    </section>
  );
}
