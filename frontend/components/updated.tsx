import { UPDATE_INTERVAL } from "$lib/src/constants";

async function getTime() {
  const resp = await fetch(
    "https://worldtimeapi.org/api/timezone/America/Los_Angeles",
    {
      next: {
        revalidate: UPDATE_INTERVAL
      }
    }
  );
  const json = await resp.json();
  const time = new Date(json.datetime);
  return time.toLocaleString() + " PST";
}

export default async function Updated() {
  const time = await getTime();
  return (
    <div className="bg-green-400 p-1 rounded-md">
      <span className="font-bold">Last updated:</span> {time}
    </div>
  );
}
