import Papa from "papaparse";
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "$lib/components/shadcn/components/ui/table";

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
  const url = `${process.env.BACKEND_URL}/api/jobs`;
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
      <Table>
        <TableHeader>
          <TableRow key={"header"}>
            {keys.map((col: any) => (
              <TableHead key={col}>{col}</TableHead>
            ))}
          </TableRow>
        </TableHeader>
        <TableBody>
          {data.map((row) => (
            <TableRow key={row.URL}>
              {Object.entries(row).map(([key, value]) => {
                switch (key) {
                  case "URL":
                    return (
                      <TableCell key={value} className="px-6 py-4">
                        <a className="underline" href={value} target="_blank">
                          Apply
                        </a>
                      </TableCell>
                    );
                  default:
                    return (
                      <TableCell key={value} className="px-6 py-4">
                        {value}
                      </TableCell>
                    );
                }
              })}
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  );
}
