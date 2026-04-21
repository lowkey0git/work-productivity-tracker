# Work Productivity Tracker

## Comprehensive Documentation

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/lowkey0git/work-productivity-tracker.git
   ```
2. Navigate into the directory:
   ```bash
   cd work-productivity-tracker
   ```
3. Install the required dependencies:
   ```bash
   npm install
   ```

### Setup
- Ensure you have Node.js and npm installed. Recommended Node version: 14.x.x or later.
- Create a `.env` file in the root directory based on the `.env.example` file provided. Configure your environment variables as needed.

### API Endpoints
- **GET /api/tasks**: Retrieve all tasks.
- **POST /api/tasks**: Create a new task.
- **GET /api/tasks/:id**: Retrieve a task by ID.
- **PUT /api/tasks/:id**: Update a task by ID.
- **DELETE /api/tasks/:id**: Delete a task by ID.

### Usage Examples
1. **Retrieve All Tasks**:
   ```bash
   curl -X GET http://localhost:3000/api/tasks
   ```
2. **Create a New Task**:
   ```bash
   curl -X POST http://localhost:3000/api/tasks -H 'Content-Type: application/json' -d '{"title": "New Task", "description": "Task description"}'
   ```
3. **Update a Task**:
   ```bash
   curl -X PUT http://localhost:3000/api/tasks/1 -H 'Content-Type: application/json' -d '{"title": "Updated Task"}'
   ```
4. **Delete a Task**:
   ```bash
   curl -X DELETE http://localhost:3000/api/tasks/1
   ```

### Conclusion
This tracker helps manage your tasks effectively and improve productivity. For further information, consult the source code or contact the maintainer.