import { useAuth } from '@/hooks/useAuth';
import { useState } from 'react';
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import Header from '@/components/Header';
import { ShoppingCart } from 'lucide-react';
import PurchaseRequestForm from '@/components/PurchaseRequestForm';

const Index = () => {
  const { user, logout } = useAuth();
  const [activeTab, setActiveTab] = useState('requests');

  const handleLogout = () => {
    logout();
    setActiveTab('requests');
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <Header user={user} onLogout={handleLogout} />
      
      <div className="container mx-auto px-4 py-6">
        <Tabs value={activeTab} onValueChange={setActiveTab} className="w-full">
          <TabsList className="grid w-full grid-cols-1 mb-1"> {/* alterar grid-cols-n para o número correspondente de itens apresentados */}
            
            <TabsTrigger value="purchase" className="flex items-center space-x-2">
              <ShoppingCart className="h-3 w-3" />
              <span className="hidden sm:inline">Editar Solicitação de Compras</span>
              <span className="sm:hidden">Compras</span>
            </TabsTrigger>

          </TabsList>

          <TabsContent value="purchase" className="space-y-4">
            <PurchaseRequestForm user={user} />
          </TabsContent>

        </Tabs>
      </div>
    </div>
  );
};

export default Index;
