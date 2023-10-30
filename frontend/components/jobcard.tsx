import {
  Card,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "$lib/components/shadcn/components/ui/card";
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "$lib/components/shadcn/components/ui/tooltip";
import { Job } from "$lib/components/table";
import { BackpackIcon, ClockIcon } from "@radix-ui/react-icons";
import dayjs from "dayjs";
import isToday from "dayjs/plugin/isToday";
import isTomorrow from "dayjs/plugin/isTomorrow";
import isYesterday from "dayjs/plugin/isYesterday";
import relativeTime from "dayjs/plugin/relativeTime";
import Link from "next/link";

dayjs.extend(relativeTime);
dayjs.extend(isYesterday);
dayjs.extend(isToday);
dayjs.extend(isTomorrow);

export default function JobCard(props: Job) {
  return (
    <Link href={props.URL} target="_blank">
      <Card className="h-full">
        <CardHeader>
          <CardTitle>{props.Title}</CardTitle>
          <CardDescription>
            {props.Company}
            {props["Years of Experience"]
              ? ` • ${props["Years of Experience"]} YOE`
              : ""}
          </CardDescription>
        </CardHeader>
        <CardFooter className="flex flex-col items-start">
          <CardDescription>
            <span className="flex items-center gap-1">
              <BackpackIcon />
              {props.Location}
            </span>
          </CardDescription>
          <CardDescription>
            <TooltipProvider>
              <Tooltip>
                <TooltipTrigger>
                  <div className="flex items-center gap-1">
                    <ClockIcon />
                    {getRelativeDateString(props.Date)}
                  </div>
                </TooltipTrigger>
                <TooltipContent>{props.Date}</TooltipContent>
              </Tooltip>
            </TooltipProvider>
          </CardDescription>
        </CardFooter>
      </Card>
    </Link>
  );
}

function getRelativeDateString(date: string) {
  const now = dayjs();
  const d = dayjs(date);
  if (d.isToday() || d.isTomorrow()) {
    return "Today";
  } else if (d.isYesterday()) {
    return "Yesterday";
  } else {
    return d.fromNow();
  }
}
