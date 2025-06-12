
import React from 'react';
import { Button } from "@/components/ui/button";
import { LogOut, User } from 'lucide-react';

interface HeaderProps {
  user: { name: string; email: string } | null;
  onLogout: () => void;
}

const Header: React.FC<HeaderProps> = ({ user, onLogout }) => {
  return (
    <header className="bg-blue-600 text-white shadow-lg">
      <div className="container mx-auto px-4 py-4 flex justify-between items-center">
        <h1 className="text-2xl font-bold">Sistema de Solicitações</h1>
        {user && (
          <div className="flex items-center space-x-4">
            <div className="flex items-center space-x-2">
              <User className="h-5 w-5" />
              <span className="font-medium">{user.name}</span>
            </div>
            <Button 
              variant="outline" 
              size="sm" 
              onClick={onLogout}
              className="bg-white text-blue-600 hover:bg-blue-50"
            >
              <LogOut className="h-4 w-4 mr-2" />
              Sair
            </Button>
          </div>
        )}
      </div>
    </header>
  );
};

export default Header;
