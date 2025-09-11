import { useState } from "react";
import { Button } from "./ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "./ui/card";
import { Input } from "./ui/input";
import { Label } from "./ui/label";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "./ui/select";
import { Textarea } from "./ui/textarea";
import { CalendarIcon, Plus, Trash2, Package } from "lucide-react";
import { Popover, PopoverContent, PopoverTrigger } from "./ui/popover";
import { Calendar } from "./ui/calendar";
import { format } from "date-fns";
import { ptBR } from "date-fns/locale";
import { cn } from "@/lib/utils";
import { useToast } from "@/hooks/use-toast";

interface RequestItem {
  id: string;
  produto: string;
  armazem: string;
  quantidade: number;
  previsaoInicio: Date | undefined;
  dataEntrega: Date | undefined;
  dataEmissao: Date | undefined;
  tipoOP: string;
  observacao: string;
}

export const RequestForm = () => {
  const { toast } = useToast();
  const [items, setItems] = useState<RequestItem[]>([{
    id: '1',
    produto: '',
    armazem: '',
    quantidade: 0,
    previsaoInicio: undefined,
    dataEntrega: undefined,
    dataEmissao: new Date(),
    tipoOP: '',
    observacao: ''
  }]);

  const addItem = () => {
    const newItem: RequestItem = {
      id: Date.now().toString(),
      produto: '',
      armazem: '',
      quantidade: 0,
      previsaoInicio: undefined,
      dataEntrega: undefined,
      dataEmissao: new Date(),
      tipoOP: '',
      observacao: ''
    };
    setItems([...items, newItem]);
  };

  const removeItem = (id: string) => {
    if (items.length > 1) {
      setItems(items.filter(item => item.id !== id));
    }
  };

  const updateItem = (id: string, field: keyof RequestItem, value: any) => {
    setItems(items.map(item => 
      item.id === id ? { ...item, [field]: value } : item
    ));
  };

  const handleSubmit = () => {
    const hasEmptyFields = items.some(item => 
      !item.produto || !item.armazem || !item.quantidade || !item.tipoOP
    );

    if (hasEmptyFields) {
      toast({
        title: "Erro",
        description: "Por favor, preencha todos os campos obrigatórios.",
        variant: "destructive"
      });
      return;
    }

    toast({
      title: "Solicitação enviada!",
      description: "Sua solicitação foi enviada para aprovação.",
      variant: "default"
    });
  };

  const DatePickerField = ({ 
    value, 
    onChange, 
    placeholder 
  }: { 
    value: Date | undefined; 
    onChange: (date: Date | undefined) => void; 
    placeholder: string;
  }) => (
    <Popover>
      <PopoverTrigger asChild>
        <Button
          variant="outline"
          className={cn(
            "w-full justify-start text-left font-normal",
            !value && "text-muted-foreground"
          )}
        >
          <CalendarIcon className="mr-2 h-4 w-4" />
          {value ? format(value, "dd/MM/yyyy", { locale: ptBR }) : placeholder}
        </Button>
      </PopoverTrigger>
      <PopoverContent className="w-auto p-0" align="start">
        <Calendar
          mode="single"
          selected={value}
          onSelect={onChange}
          initialFocus
          className="p-3 pointer-events-auto"
        />
      </PopoverContent>
    </Popover>
  );

  return (
    <Card className="w-full">
      <CardHeader>
        <CardTitle className="flex items-center space-x-2">
          <Package className="h-6 w-6 text-blue-600" />
          <span>Nova Solicitação de Conjuntos de Reparo</span>
        </CardTitle>
      </CardHeader>
      <CardContent>
        <form onSubmit={e => { e.preventDefault(); handleSubmit(); }} className="space-y-6">
          <div className="space-y-4">
            {items.map((item, idx) => (
              <div key={item.id} className="grid grid-cols-1 md:grid-cols-12 gap-4 items-end border p-4 rounded-md bg-gray-50 relative">
                <div className="grid grid-cols-1 md:grid-cols-11 md:col-span-11 gap-4">
                  <div className="md:col-span-5 space-y-2">
                    <Label htmlFor={`produto-${item.id}`}>Produto *</Label>
                    <Input
                      id={`produto-${item.id}`}
                      value={item.produto}
                      onChange={(e) => updateItem(item.id, 'produto', e.target.value)}
                      placeholder="Descreva o produto ou serviço"
                      required
                    />
                  </div>
                  <div className="md:col-span-3 space-y-2">
                    <Label htmlFor={`armazem-${item.id}`}>Armazém *</Label>
                    <Select
                      value={item.armazem}
                      onValueChange={(value) => updateItem(item.id, 'armazem', value)}
                    >
                      <SelectTrigger>
                        <SelectValue placeholder="Selecione um armazém" />
                      </SelectTrigger>
                      <SelectContent>
                        <SelectItem value="armazem-1">Armazém Central</SelectItem>
                        <SelectItem value="armazem-2">Armazém Norte</SelectItem>
                        <SelectItem value="armazem-3">Armazém Sul</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>
                  <div className="md:col-span-3 space-y-2">
                    <Label htmlFor={`quantidade-${item.id}`}>Quantidade *</Label>
                    <Input
                      id={`quantidade-${item.id}`}
                      type="number"
                      value={item.quantidade}
                      onChange={(e) => updateItem(item.id, 'quantidade', parseFloat(e.target.value) || 0)}
                      placeholder="0.00"
                      min="0"
                      step="0.01"
                      required
                    />
                  </div>
                  <div className="md:col-span-3 space-y-2">
                    <Label>Previsão de Início</Label>
                    <DatePickerField
                      value={item.previsaoInicio}
                      onChange={(date) => updateItem(item.id, 'previsaoInicio', date)}
                      placeholder="dd/mm/aaaa"
                    />
                  </div>
                  <div className="md:col-span-3 space-y-2">
                    <Label>Data de Entrega</Label>
                    <DatePickerField
                      value={item.dataEntrega}
                      onChange={(date) => updateItem(item.id, 'dataEntrega', date)}
                      placeholder="dd/mm/aaaa"
                    />
                  </div>
                  <div className="md:col-span-3 space-y-2">
                    <Label>Data de Emissão</Label>
                    <DatePickerField
                      value={item.dataEmissao}
                      onChange={(date) => updateItem(item.id, 'dataEmissao', date)}
                      placeholder="dd/mm/aaaa"
                    />
                  </div>
                  <div className="md:col-span-4 space-y-2">
                    <Label>Tipo da Ordem de Produção (OP) *</Label>
                    <Select
                      value={item.tipoOP}
                      onValueChange={(value) => updateItem(item.id, 'tipoOP', value)}
                    >
                      <SelectTrigger>
                        <SelectValue placeholder="Selecione o tipo de OP" />
                      </SelectTrigger>
                      <SelectContent>
                        <SelectItem value="urgente">Urgente</SelectItem>
                        <SelectItem value="normal">Normal</SelectItem>
                        <SelectItem value="programada">Programada</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>
                  <div className="md:col-span-7 space-y-2">
                    <Label htmlFor={`observacao-${item.id}`}>Observações</Label>
                    <Textarea
                      id={`observacao-${item.id}`}
                      value={item.observacao}
                      onChange={(e) => updateItem(item.id, 'observacao', e.target.value)}
                      placeholder="Informações adicionais..."
                      rows={2}
                    />
                  </div>
                </div>
                <div className="grid grid-cols-1 p-4 h-full">
                  <div className="col-span-1 md:col-span-2 flex items-center justify-center">
                    <Button
                      type="button"
                      variant="destructive"
                      className="h-10"
                      onClick={() => removeItem(item.id)}
                      disabled={items.length === 1}
                      title="Remover item"
                    >
                      <Trash2 className="w-4 h-4" />
                    </Button>
                  </div>
                </div>
              </div>
            ))}
            <Button type="button" variant="outline" onClick={addItem} className="mt-2 flex items-center gap-2">
              <Plus className="w-5 h-5" /> Adicionar Item
            </Button>
          </div>
          <div className="flex justify-end space-x-4">
            <Button type="button" variant="outline" onClick={() => setItems([{
              id: '1', produto: '', armazem: '', quantidade: 0, previsaoInicio: undefined, dataEntrega: undefined, dataEmissao: new Date(), tipoOP: '', observacao: ''
            }])}>
              Cancelar
            </Button>
            <Button type="submit" className="bg-primary hover:bg-primary/90">
              Criar Solicitação
            </Button>
          </div>
        </form>
      </CardContent>
    </Card>
  );
};