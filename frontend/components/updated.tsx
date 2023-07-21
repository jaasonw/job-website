async function getTime() {
  const resp = await fetch(
    "https://worldtimeapi.org/api/timezone/America/Los_Angeles",
    {
      next: {
        tags: ["jobs"],
        revalidate: 0,
      },
    },
  );
  const json = await resp.json();
  const time = new Date(json.datetime);
  return time.toLocaleString("en-US", { timeZone: "PST" }) + " PST";
}

export default async function Updated() {
  const time = await getTime();
  return (
    <div className="bg-green-400 p-1 rounded-md">
      <span className="font-bold">Last updated:</span> {time}
    </div>
  );
}
