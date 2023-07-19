import { NextRequest, NextResponse } from "next/server";
import { revalidateTag } from "next/cache";

export async function GET(request: NextRequest) {
  const key = request.nextUrl.searchParams.get("key");
  if (key == process.env.REVALIDATE_KEY) {
    revalidateTag("jobs");
    return NextResponse.json({ revalidated: true, now: Date.now() });
  }
  return NextResponse.json({ revalidated: false, now: Date.now() });
}
