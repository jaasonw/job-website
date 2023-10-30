import Papa from "papaparse";
import JobCard from "$lib/components/jobcard";
import { Paginated } from "./paginated";

export interface Job {
  URL: string;
  Title: string;
  Company: string;
  Date: string;
  Location: string;
  Technologies: string;
  "Years of Experience": string;
}

async function load() {
  const url = `${process.env.BACKEND_URL}/api/jobs`;
  const resp = await fetch(url, {
    cache: "no-store",
  });
  const csv = await resp.text();
  let parsed = Papa.parse(csv, { header: true });

  const data = parsed.data.map((col: any) => {
    return {
      Date: col["Date"],
      URL: col["URL"],
      Company: col["Company"] || "N/A",
      Title: col["Title"],
      Location: col["Location"],
      Technologies: col["Technologies"],
      "Years of Experience": col["Years of Experience"],
    } as Job;
  });
  return data;
}

export default async function JobsTable() {
  const data = (await load()) as Job[];
  return (
    <Paginated jobs={data} />
    // <div className="grid grid-cols-4 gap-4">
    //   {data.map((row) => (
    //     <JobCard {...row} key={row.URL} />
    //   ))}
    // </div>
  );
}
