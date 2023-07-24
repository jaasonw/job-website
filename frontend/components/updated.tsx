import Papa from "papaparse";

async function getTime() {
  const url = process.env.GOOGLE_SHEETS_METADATA_URL ?? "";
  const resp = await fetch(url, {
    next: { revalidate: 60 * 60 },
  });
  const csv = await resp.text();
  let parsed: any = Papa.parse(csv);
  if (parsed.data.length < 2) return "unknown";
  else return parsed.data[1][0];
}

export default async function Updated() {
  const time = await getTime();
  return (
    <div className="bg-green-400 p-1 rounded-md">
      <span className="font-bold">Last updated:</span> {time}
    </div>
  );
}
