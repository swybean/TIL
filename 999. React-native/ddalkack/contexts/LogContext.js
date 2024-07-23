import React from "react";
import { createContext, useState } from "react";
import { v4 as uuidv4 } from "uuid";

const LogContext = createContext();

export function LogContextProvider({ children }) {
  const [logs, setLogs] = useState([
    // 임의데이터 넣은 것임, 확인 끝나면 useState []로 다시 만들어두기
    {
      id: uuidv4(),
      title: "Log 3",
      body: "Log 3",
      date: new Date().toISOString(),
    },
    {
      id: uuidv4(),
      title: "Log 2",
      body: "Log 2",
      date: new Date(Date.now() - 1000 * 60 * 3).toISOString(),
    },
    {
      id: uuidv4(),
      title: "Log 1",
      body: "Log 1",
      date: new Date(Date.now() - 1000 * 60 * 60 * 24 * 3).toISOString(),
    },
  ]);

  const onCreate = ({ title, body, date }) => {
    const log = {
      id: uuidv4(),
      title,
      body,
      date,
    };
    setLogs([log, ...logs]);
  };

  return (
    <LogContext.Provider value={{ logs, onCreate }}>
      {children}
    </LogContext.Provider>
  );
}

export default LogContext;
