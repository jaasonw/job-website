import Papa from "papaparse";
import { Badge } from "$lib/components/shadcn/components/ui/badge";

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
    <Badge>
      <span className="font-bold">Last updated:</span>{" "}
      {metadata["last_updated"]}
    </Badge>
  );
}
