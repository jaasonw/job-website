import Papa from "papaparse";

interface Job {
  URL: string;
  Title: string;
  Company: string;
  Date: string;
  Location: string;
  Technologies: string;
  "Years of Experience": string;
}

async function load() {
  const url = process.env.GOOGLE_SHEETS_URL ?? "";
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
  const keys = Object.keys(data[0]);
  return (
    <div className="w-full h-[50vh] overflow-x-scroll overflow-y-scroll">
      <table className="w-full text-sm text-left text-gray-500 dark:text-gray-400">
        <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
          <tr>
            {keys.map((col: any) => (
              <th className="px-6 py-3">{col}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {data.map((row) => (
            <tr>
              {Object.entries(row).map(([key, value]) => {
                switch (key) {
                  case "URL":
                    return (
                      <td className="px-6 py-4">
                        <a className="underline" href={value} target="_blank">
                          Apply
                        </a>
                      </td>
                    );
                  default:
                    return <td className="px-6 py-4">{value}</td>;
                }
              })}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
