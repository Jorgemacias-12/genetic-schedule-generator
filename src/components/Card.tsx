import React from "react";

interface Props {
  customClassNames?: string;
  children?: React.ReactNode;
}

export const Card = ({ customClassNames, children }: Props) => {
  return (
    <article
      className={`${customClassNames} border bg-white p-2 rounded-md shadow-md`}
    >
      {children}
    </article>
  );
};
