import { Badge } from "$lib/components/shadcn/components/ui/badge";

async function getMetadata() {
  const url = `${process.env.BACKEND_URL}/api/stats` ?? "";
  const resp = await fetch(url, {
    cache: "no-store",
  });
  const data = await resp.text();
  let parsed: any = JSON.parse(data);
  return parsed;
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
