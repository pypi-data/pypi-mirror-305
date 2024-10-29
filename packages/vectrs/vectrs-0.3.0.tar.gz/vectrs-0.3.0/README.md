# Vectrs - Decentralized & Distributed Vector Database   [![Downloads](https://static.pepy.tech/badge/vectrs)](https://pepy.tech/project/vectrs)

## Overview   
**Vectrs** is a decentralized & distributed vector database designed for efficient storage and retrieval of vector embeddings. It combines P2P networking with advanced vector operations, RAG capabilities, and graph-based relationships, making it ideal for AI-powered distributed applications.

## Features   
- **Distributed Architecture**
  - P2P network with load balancing
  - Data replication for fault tolerance
  - Horizontal scalability
  
- **Vector Operations**
  - Multiple similarity metrics (L2, cosine, etc.)
  - Different index types (HNSW, Graphine)
  - Batch vector operations
  - Vector metadata support
  
- **Graph Capabilities**
  - Vector relationships management
  - Graph-based queries
  - Customizable relationship types
  
- **AI Integration**
  - RAG (Retrieval-Augmented Generation) workflow
  - Custom agent creation and management
  - Task analysis capabilities

## Installation   
```bash
pip install vectrs
```

## Usage

### Basic Operations

1. **Initialize and Start a Node**
```python
import asyncio
from vectrs.network import KademliaNode
from vectrs.database import VectorDBManager

async def start_node():
    # Initialize node
    node = KademliaNode(host='127.0.0.1', port=8468)
    db_manager = VectorDBManager()
    node.set_local_db_manager(db_manager)
    
    # Start node
    await node.start()
    
    # Optional: Connect to existing network
    await node.bootstrap('bootstrap_host', 8468)
    return node

# Run the node
node = asyncio.run(start_node())
```

2. **Create Database**
```python
async def create_database(node):
    db_manager = VectorDBManager()
    # Create database with HNSW index
    db_id = db_manager.create_database(
        dim=1024,
        space=SimilarityMetric.L2,
        max_elements=10000,
        index_type=IndexType.HNSW
    )
    return db_id

db_id = asyncio.run(create_database(node))
```

3. **Vector Operations**
```python
import numpy as np

async def vector_operations(node, db_id):
    # Add vector
    vector = np.random.rand(1024).astype(np.float32)
    metadata = {"description": "example vector"}
    await node.add_vector(db_id, "vector1", vector, metadata)

    # Query vector
    results = await node.query_vector(db_id, "vector1", k=10)
    
    # Batch add vectors
    vectors = {
        "vec1": np.random.rand(1024).astype(np.float32),
        "vec2": np.random.rand(1024).astype(np.float32)
    }
    metadata_list = [{"desc": "vec1"}, {"desc": "vec2"}]
    await node.batch_add_vectors(db_id, vectors, metadata_list)
    
    # Update vector
    new_vector = np.random.rand(1024).astype(np.float32)
    await node.update_vector(db_id, "vector1", new_vector, {"updated": True})
    
    # Delete vector
    await node.delete_vector(db_id, "vector1")

asyncio.run(vector_operations(node, db_id))
```

### Graph Operations
```python
async def graph_operations(node, db_id):
    # Add relationship between vectors
    await node.add_relationship(
        db_id, 
        "vector1", 
        "vector2", 
        relationship_type="similar_to"
    )
    
    # Get relationships
    relationships = await node.get_relationships(db_id, "vector1")
    
    # Graph-based query
    results = await node.query_with_graph(
        db_id,
        "vector1",
        k=10,
        max_depth=2
    )

asyncio.run(graph_operations(node, db_id))
```

### AI and RAG Features
```python
from vectrs.swarm import Swarm

async def ai_operations(node):
    # Initialize Swarm
    swarm = Swarm(node.db_manager, host='127.0.0.1', port=8468)
    await swarm.initialize()
    
    # Run RAG workflow
    result = await swarm.run_rag_workflow(
        query="What is the relationship between these vectors?"
    )
    
    # Create and manage AI agent
    agent = await swarm.create_custom_agent(
        agent_type="analyzer",
        agent_id="agent1"
    )
    
    # Check agent status
    status = await swarm.get_agent_status("agent1")
    
    # Analyze task
    analysis = await swarm.analyze_task({
        "type": "vector_analysis",
        "data": "Sample data"
    })

asyncio.run(ai_operations(node))
```

### Advanced Features

#### Graphine Search
```python
async def graphine_search(node, db_id):
    results = await node.graphine_search(
        db_id=db_id,
        vector_id="vector1",
        k=10,
        ef=50
    )
    return results

asyncio.run(graphine_search(node, db_id))
```

## API Reference

For detailed API documentation and advanced usage, visit our [documentation](https://github.com/ParalexLabs/Vectrs-beta/docs).

## Contributing
Contributions are welcome! Please check our [contribution guidelines](CONTRIBUTING.md).

## License   
Apache License 2.0. See [LICENSE](LICENSE) for details.

## Support   
- GitHub Issues: [Vectrs-beta Issues](https://github.com/ParalexLabs/Vectrs-beta/issues)
- Email: sakib@paralex.tech
- Version: 0.3.0
