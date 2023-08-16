from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI()

class InvoiceData(BaseModel):
    invoice_doc: str
    invoice_date: datetime
    invoice_due_date: datetime
    faktur_pajak_no: str
    ppn_rate: float
    description: str

class InvoiceListDetail(BaseModel):
    doc_received_no: str
    po_no: str
    item: str
    quantity: int
    amount_dpp: float
    other_amount: float
    ppn_amount: float
    pph_prepaid: float
    pph_payable: float
    total_before_tax: float
    total_after_tax: float
class TransactionData(BaseModel):
    bds_doc_no: str
    bds_doc_date: datetime
    supplier: str
    supplier_tax_id: str
    transaction_type: str
    bank_name: str
    bank_account: str
    bank_account_name: str
    support_doc: str
    payment_plan_date: datetime
    paid_date: datetime
    invoice_data: InvoiceData
    invoice_detail: List[InvoiceListDetail]


@app.post("/submit_transaction/")
async def submit_transaction(data: TransactionData):
    # Here you can perform any processing or database operations with the submitted data
    # For now, let's just return the received data
    return {"message": "Transaction submitted successfully", "data": data.dict()}
