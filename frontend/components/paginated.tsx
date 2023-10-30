"use client";
import { Job } from "$lib/components/table";
import { useState } from "react";
import JobCard from "$lib/components/jobcard";
import { Button } from "$lib/components/shadcn/components/ui/button";

export function Paginated(props: { jobs: Job[] }) {
  const numPerPage = 12;
  const totalPages = Math.ceil(props.jobs.length / numPerPage);
  let [page, setPage] = useState(0);
  let startingIndex = page * numPerPage;
  let endingIndex = startingIndex + numPerPage;
  let jobs = props.jobs.slice(startingIndex, endingIndex);
  return (
    <div className="flex flex-col justify-between gap-4 w-full">

      <div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
        {jobs.map((row) => (
          <JobCard {...row} key={row.URL} />
        ))}
      </div>
      <div className="flex justify-center gap-2">
        <Button
          // variant="outline"
          // size="icon"
          onClick={() => setPage(page - 1)}
          disabled={page == 0}
        >
          Previous
        </Button>
        <Button
          // variant="outline"
          // size="icon"
          onClick={() => setPage(page + 1)}
          disabled={page == totalPages - 1}
        >
          Next
        </Button>
      </div>
    </div>
  );
}
