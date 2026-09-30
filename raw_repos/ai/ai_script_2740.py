import torch

# Load the dataset
train_data, valid_data, test_data = torch.utils.data.random_split(dataset, (1000, 400, 200))

# Build the model
model = torch.nn.Sequential(
    torch.nn.Linear(7, 15), 
    torch.nn.ReLU(), 
    torch.nn.Linear(15, 4), 
    torch.nn.Softmax()
)

# Compile the model
criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Train the model
model.train()
for epoch in range(10):
    loss = 0
    for data, target in train_loader:
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss += criterion(output, target).item()
        loss.backward()
        optimizer.step()
    
    print(f'Epoch: {epoch}, Loss: {loss/len(train_data)}')