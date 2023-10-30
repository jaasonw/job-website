async function getMetadata() {
  const url = `${process.env.BACKEND_URL}/api/stats` ?? "";
  const resp = await fetch(url, {
    cache: "no-store",
  });
  const data = await resp.text();
  let parsed: any = JSON.parse(data);
  return parsed;
}

export default async function Stats() {
  const metadata = await getMetadata();
  return (
    <section className="flex flex-col items-center text-center">
      <h1 className="text-3xl text-center font-bold">Filter Stats</h1>
      <div className="grid md:grid-cols-4 grid-cols-1 gap-3">
        <div className="flex flex-col items-center text-center">
          <span className="text-5xl font-medium">
            {metadata["total_count"]}
          </span>
          <span className="">Listings Processed</span>{" "}
        </div>
        <div className="flex flex-col items-center text-center">
          <span className="text-5xl font-medium">
            {metadata["mid_count"] + metadata["senior_count"]}
          </span>
          <span className="">Mid-Senior Positions</span>{" "}
        </div>
        <div className="flex flex-col items-center text-center">
          <span className="text-5xl font-medium">{metadata["ts_sci_count"]}</span>
          <span className="">TS/SCI Positions</span>{" "}
        </div>
        <div className="flex flex-col items-center text-center">
          <span className="text-5xl font-medium">{metadata["blacklist_count"]}</span>
          <span className="">
            Blacklisted Companies
          </span>{" "}
        </div>
      </div>
    </section>
  );
}
