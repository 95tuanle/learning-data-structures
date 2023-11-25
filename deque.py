from collections import deque

printer_queue = deque()
printer_queue.append("TaylorSwiftTickets.pdf")
printer_queue.append("MarketingNotes.pdf")
printer_queue.append("Proof.pdf")

while len(printer_queue) > 0:
    document = printer_queue.popleft()
    print(f'Printing {document}')
