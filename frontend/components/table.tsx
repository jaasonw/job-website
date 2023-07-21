import { UPDATE_INTERVAL } from "$lib/src/constants";
import Papa from "papaparse";

async function load() {
  const url = process.env.GOOGLE_SHEETS_URL ?? "";
  const resp = await fetch(url, {
    next: {
      tags: ["jobs"],
      revalidate: 0,
    },
  });
  const csv = await resp.text();
  let parsed = Papa.parse(csv);
  console.log(parsed.data[0]);

  // remove 4th column from data
  parsed.data = parsed.data.map((col: any) =>
    col.filter((_: any, i: number) => i !== 4),
  );
  return parsed.data;
}

export default async function JobsTable() {
  const data = (await load()) as any[];
  return (
    <div className="w-full overflow-x-scroll h-96 overflow-y-scroll">
      <table className="w-full text-sm text-left text-gray-500 dark:text-gray-400">
        <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
          <tr>
            {data[0].map((col: any) => (
              <th className="px-6 py-3">{col}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {data.slice(1).map((row: any) => (
            <tr>
              {row.map((col: any, i: number) =>
                i == 0 ? (
                  <td className="px-6 py-4">
                    <a className="underline" href={col} target="_blank">
                      Apply
                    </a>
                  </td>
                ) : (
                  <td className="px-6 py-4">{col}</td>
                ),
              )}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
