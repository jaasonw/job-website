import Papa from "papaparse";

async function getMetadata() {
  const url = process.env.GOOGLE_SHEETS_METADATA_URL ?? "";
  const resp = await fetch(url, {
    cache: "no-store",
  });
  const csv = await resp.text();
  let parsed: any = Papa.parse(csv, { header: true });
  return parsed.data[0];
}

export default async function Stats() {
  const metadata = await getMetadata();
  return (
    <section className="flex flex-col items-center text-center">
      <h1 className="text-3xl text-center font-bold">Filter Stats</h1>
      <div className="grid md:grid-cols-3 grid-cols-1 gap-3">
        <div className="flex flex-col items-center text-center">
          <span className="text-5xl font-medium">
            {metadata["high_experience"]}
          </span>
          <span className="">Mid-Senior Positions</span>{" "}
        </div>
        <div className="flex flex-col items-center text-center">
          <span className="text-5xl font-medium">{metadata["ts_sci"]}</span>
          <span className="">TS/SCI Positions</span>{" "}
        </div>
        <div className="flex flex-col items-center text-center">
          <span className="text-5xl font-medium">{metadata["blacklist"]}</span>
          <span className="">
            Blacklisted Companies and Recruiting Agencies
          </span>{" "}
        </div>
      </div>
    </section>
  );
}
