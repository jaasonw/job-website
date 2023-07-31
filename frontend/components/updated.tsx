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

export default async function Updated() {
  const metadata = await getMetadata();
  return (
    <div className="bg-green-400 p-1 rounded-md">
      <span className="font-bold">Last updated:</span>{" "}
      {metadata["last_updated"]}
    </div>
  );
}
