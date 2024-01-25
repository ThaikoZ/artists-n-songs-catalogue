import React, { PropsWithChildren } from "react";

const Container = ({ children }: PropsWithChildren) => {
  return (
    <div className="flex container justify-center min-w-[350px]">
      {children}
    </div>
  );
};

export default Container;
