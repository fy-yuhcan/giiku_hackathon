"use client";

import React from 'react';
import { useState, createContext, ReactNode } from "react";


export type User = { user_id: number, name: string, password: string }
export type pageContextType = {
  user: User;
  setUser: (user: User) => void;
}


export const UserContext = createContext<pageContextType>({user: {user_id: 9999, name: "default", password: "defualt"}, setUser: (user) => user});


export const UserProvider = ({children}) => {
    const [user, setUser] = useState<User>({user_id: 9999, name: "default", password: "defualt"})

  return (
    <UserContext.Provider value={{user, setUser}}>
      {children}
    </UserContext.Provider>
  );
}