"use client";

import React from 'react';
import { useState, createContext, ReactNode } from "react";


export type User = { user_id: number, name: string, password: string, isLogin: boolean }
export type UserContextType = {
  user: User;
  setUser: (user: User) => void;
}


export const UserContext = createContext<UserContextType>({user: {user_id: 1, name: "default", password: "defualt", isLogin: false}, setUser: (user) => user});


export const UserProvider = ({children}) => {
    const [user, setUser] = useState<User>({user_id: 1, name: "default", password: "defualt", isLogin: false})

  return (
    <UserContext.Provider value={{user, setUser}}>
      {children}
    </UserContext.Provider>
  );
}