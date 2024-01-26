import React, { PropsWithChildren } from "react";

const Container = ({ children }: PropsWithChildren) => {
  return (
    <div className="flex flex-grow ">
      <div className="flex container h-fit justify-center min-w-[350px]">
        {children}
      </div>
    </div>
  );
};

export default Container;
