import React, { PropsWithChildren } from "react";

const ContentCard = ({ children }: PropsWithChildren) => {
  return (
    <div className="flex flex-col gap-3 rounded-md max-w-5xl shadow-md p-5 w-full bg-white">
      {children}
    </div>
  );
};

export default ContentCard;
